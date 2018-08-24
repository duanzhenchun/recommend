import math
import numpy as np
from scipy.spatial import distance

class UserBasedCF(object):
    def __init__(self, train_file):
        self.train_file = train_file
        self.readData()
        self.UserSimilarity_cosin()
        # self.UserSimilarity_euclidean()

    def readData(self):
        self.user_item = dict()
        with open(self.train_file, "r", encoding="utf-8") as f:
            for line in f:
                user, item, score, _ = line.strip().split("\t")
                self.user_item.setdefault(user, {})
                self.user_item[user][item] = int(score)


    def UserSimilarity_cosin(self):
        self.item_user = dict()
        for user, items in self.user_item.items():
            for i in items.keys():
                if i not in self.item_user:
                    self.item_user[i] = set()
                self.item_user[i].add(user)

        C = dict()     # 用户-用户共现矩阵
        for user in self.item_user.values():
            for u in user:
                C.setdefault(u, {})
                for v in user:
                    if u == v:
                        continue
                    C[u].setdefault(v, 0)
                    C[u][v] += 1
        # print(C["1"]["2"])
        # print("------------------------------------")

        self.W = dict()
        for u, related_users in C.items():
            self.W.setdefault(u, {})
            for v, cuv in related_users.items():
                self.W[u][v] = cuv / math.sqrt(len(self.user_item[u]) * len(self.user_item[v]))

        return self.W

    # def UserSimilarity_euclidean(self):
    #     self.W = dict()
    #     for u in self.user_item.keys():
    #         self.W.setdefault(u, {})
    #         for v in self.user_item.keys():
    #             self.W[u].setdefault(v, 0)
    #             sim = {}
    #             for item in self.user_item[u]:
    #                 if item in self.user_item[v]:
    #                     sim[item] =1
    #             self.W[u][v] = 1/(1+math.sqrt(sum([pow(self.user_item[u][item] - self.user_item[v][item], 2) for item in sim])))
    #     print(self.W["1"]["2"])
    #     return self.W

    def Recommend(self, user, K=2, N=5):
        rank = dict()
        action_item = self.user_item[user].keys()

        for v, wuv in sorted(self.W[user].items(), key=lambda x: x[1], reverse=True)[0:K]:
            for i, rvi in self.user_item[v].items():
                if i in action_item:
                    continue
                rank.setdefault(i, 0)
                rank[i] += wuv * rvi
        return list(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])


if __name__ == "__main__":
    ucf = UserBasedCF("./ml-100k/u1.base")
    print(ucf.Recommend("2"))