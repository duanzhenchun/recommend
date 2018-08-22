import numpy as np
import pandas as pd


class ItemBasedCF(object):
    def __init__(self):
        self.data = pd.read_csv("./ml-100k/u1.base", sep="\t", names=["user id", "item id", "rate", "timestamp"])
        self.data = self.data.drop(labels=["timestamp"], axis=1)
        self.user_list = []
        self.item_list = []

        for user, item in zip(self.data.iloc[:, 0], self.data.iloc[:, 1]):
            if user not in self.user_list:
                self.user_list.append(user)
            if item not in self.item_list:
                self.item_list.append(item)

    def user_item_matrix(self):
        matrix = np.zeros(len)








if __name__ == "__main__":
    cf = ItemBasedCF()
    print(cf.data)
    print(len(cf.user_list))
    print(len(cf.item_list))