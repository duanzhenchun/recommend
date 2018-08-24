import numpy as np

# 生成原始数据，用于测试
def loadDataSet():
    return [[1, 3, 4],
            [2, 3, 5],
            [1, 2, 3, 5],
            [2, 5]]


def createC1(dataSet):
    # 遍历数据集，建立1—项集
    C1 = []
    # 循环交易列表
    for transation in dataSet:
        # 循环每个交易列表的商品
        for item in transation:
            if [item] not in C1:
                # 将该商品加入C1 项集
                C1.append([item])
    # 对所有物品排序
    C1.sort()
    # 将列表元素映射到frozenset(),返回列表，frozenset()集合一旦建立就不能修改
    return list(map(frozenset, C1))


def scanD(D, Ck, minSupport):
    """
    :param D:  dataset
    :param Ck:
    :param minSupport:
    :return:
    """

    ssCnt = {}
    # key:候选集中的item   item.type = set
    # value:对应item出现的次数

    # 遍历每个交易记录
    for tid in D:
        # 遍历候选集Ck中的每一项
        for can in Ck:
            # 如果Ck中该项can在tid中出现，则当前项can是tid的子集
            if can.issubset(tid):
                if can not in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1

    # 数据集的总记录数，物品购买记录数，用来计算支持度
    numItems = float(len(D))

    # 记录最小支持度过滤后的频繁项集
    retList = []

    supportData = {}
    # key:候选集中的项
    # value: 对应的支持度
    # 遍历候选集中的每项出现次数
    for k in ssCnt.keys():
        # 计算每项的支持度
        support = ssCnt[k]/numItems
        # 支持度过滤
        if support >= minSupport:
            retList.insert(0, k)
        supportData[k] = support  # 保存了过滤前后的项集及其支持度
    return retList, supportData





def aproori(dataSet, miniSupport = 0.5):
    # 生成1项集
    C1 = createC1(dataSet)
    # 对数据映射至D，去掉重复的数据
    D = list(map(set, dataSet))

    # 过滤最小支持度，得到频繁1项集及每项支持度
    L1, supportData = scanD(D, C1, miniSupport)
    for ll in L1:
        print(ll)
    print(supportData)



if __name__ == "__main__":
    dataSet = loadDataSet()
    aproori(dataSet)

