import math
class ItemBasedCF(object):
    def __init__(self, train_file):
        # 训练数据
        self.train_file = train_file
        # 读取数据
        self.readData()
        self.ItemSimilarity_cosin()

    def readData(self):
        # 读取数据生成 user-item 的评分表
        self.user_item = dict()
        with open(self.train_file, "r", encoding="utf-8") as f:
            for line in f:
                # print(line.strip().split("\t"))
                # 获得用户、商品、评分数据， 丢弃无关的时间戳数据
                user, item, score, _ = line.strip().split("\t")
                # user-item 评分矩阵
                self.user_item.setdefault(user, {})
                # 分数赋值
                self.user_item[user][item] = int(score)

    def ItemSimilarity_cosin(self):
        # 建立物品-物品共现矩阵
        C = dict()            # 物品-物品共现矩阵
        N = dict()            # 物品被多少个不同用户购买

        # 遍历训练数据，获得用户有过行为的物品
        for user, items in self.user_item.items():
            # 遍历该用户每件物品项
            for i in items.keys():
                # 统计该物品被用户购买计数加1
                N.setdefault(i, 0)
                N[i] += 1
                # 物品-物品共现矩阵数据加1
                C.setdefault(i, {})
                # 遍历该用户每件物品项
                for j in items.keys():
                    # 若物品项为当前，跳过
                    if i == j:
                        continue
                    C[i].setdefault(j, 0)
                    C[i][j] += 1

        # 计算相似度矩阵【余弦相似度】
        self.W = dict()
        for i, related_items in C.items():
            self.W.setdefault(i, {})
            for j, cij in related_items.items():
                self.W[i][j] = cij / (math.sqrt(N[i] * N[j]))

        return self.W


    def Recommend(self, user, K=3, N=5):
        # 用户对物品的偏好值
        rank = dict()
        # 用户产生过行为的物品和评分
        action_item = self.user_item[user]

        # 找到用户产生过行为的物品，分别找到物品按相似度从大到小进行排序，取前K个相似度最大的物品推荐
        for item, score in action_item.items():
            for j, wj in sorted(self.W[item].items(), key=lambda x: x[1], reverse=True)[0:K]:
                if j in action_item.keys():
                    continue
                rank.setdefault(j, 0)
                rank[j] += score * wj
        return list(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])

if __name__ == "__main__":
    icf = ItemBasedCF("./ml-100k/u1.base")
    print(icf.Recommend("3"))