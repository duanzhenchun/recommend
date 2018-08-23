import math
import numpy as np
from scipy.spatial import distance

class UserBasedCF(object):
    def __init__(self, train_file):
        self.train_file = train_file
        self.readData()
        self.UserSimilarity()

    def readData(self):
        self.train = dict()
        with open(self.train_file, "r", encoding="utf-8") as f:
            for line in f:
                user, item, score, _ = line.strip().split(",")
                self.train.setdefault(user, {})
                self.train[user][item] = int(score)


    def UserSimilarity(self, method=1):
        self.item_user = dict()
        for user, items in self.train.items():
            for i in items.keys():
                if i not in self.item_user:
                    self.item_user[i] = set()
                self.item_user[i].add(user)

        if method ==1:
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
                    self.W[u][v] = cuv / math.sqrt(len(self.train[u]) * len(self.train[v]))

        # if method ==2:
        #     Cor = dict()
        #     for i, user in self.item_user.items():
        #         for u in user:
        #             N.setdefault(u, 0)
        #             N[u] += 1
        #
        #             # 构建用户关系矩阵
        #             Cor.setdefault(u, [])
        #             for v in user:
        #                 if u == v:
        #                     continue
        #                 Cor[u].append(v)
        #     self.Ecu = dict()
        #     for u, items in Cor.items():
        #         self.Ecu.setdefault(u, {})
        #         for v in items:
        #             self.Ecu[u][v] = 1



        return self.W


    def Recommend(self, user, K=2, N=1):
        rank = dict()
        action_item = self.train[user].keys()

        for v, wuv in sorted(self.W[user].items(), key=lambda x: x[1], reverse=True)[0:K]:
            for i, rvi in self.train[v].items():
                if i in action_item:
                    continue
                rank.setdefault(i, 0)
                rank[i] += wuv * rvi
        return list(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])


if __name__ == "__main__":
    ucf = UserBasedCF("./ml-100k/ux.data")
    print(ucf.Recommend("2"))