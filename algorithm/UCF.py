import math

class UserBasedCF(object):
    def __init__(self, train_file):
        self.train_file = train_file
        self.readData()

    def readData(self):
        self.train = dict()
        with open(self.train_file, "r", encoding="utf-8") as f:
            for line in f:
                user, item, score, _ = line.strip().split("\t")
                self.train.setdefault(user, {})
                self.train[user][item] = int(score)

    def UserSimilarity(self):
        self.item_user = dict()
        for user, items in self.train.items():
            for i in items.keys():
                if i not in self.item_user:
                    self.item_user[i] = set()
                self.item_user[i].add(user)

        C = dict()     # 用户-用户共现矩阵
        N = dict()     # 统计用户action次数

        for i, user in self.item_user.items():
            for u in user:
                N.setdefault(u, 0)
                N[u] += 1

                C.setdefault(u, {})
                for v in user:
                    if u == v:
                        continue
                    C[u].setdefault(v, 0)
                    C[u][v] += 1

        self.W = dict()
        for u, related_users in C.items():
            self.W.setdefault(u, {})
            for v, cuv in related_users.items():
                self.W[u][v] = cuv / math.sqrt(N[u] * N[v])
        return self.W


    def Recommend(self, user, K=3, N=10):
        rank = dict()
        action_item = self.train[user].keys()

        for v, wuv in sorted(self.W[user].items(), key=lambda x: x[1], reverse=True)[0:K]:
            for i, rvi in self.train[v].items():
                if i in action_item:
                    continue
                rank.setdefault(i, 0)
                rank[i] = wuv * rvi
        return list(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])


if __name__ == "__main__":
    ucf = UserBasedCF("./ml-100k/u.data")
    ucf.UserSimilarity()
    print(ucf.Recommend("3"))