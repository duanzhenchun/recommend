import jieba
import os
import re


class PreFile(object):
    def __init__(self):
        self.file_list = os.listdir(".")[0:4]
        self.result = []
        self.tag()
        self.save()
        print(self.result[0])

    def tag(self):
        for file in self.file_list:
            seg_result = {}
            seg_result_filter ={}
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    line = re.sub("\s", "", line)
                    seg_list = jieba.cut(line)
                    for seg in seg_list:
                        if seg not in seg_result.keys():
                            seg_result[seg] = 1
                        else:
                            seg_result[seg] += 1
            for k, v in seg_result.items():
                if v <= 2:
                    continue
                seg_result_filter[k] = v
            self.result.append(seg_result_filter)

    def save(self):
        with open("./index_cut.txt", "w", encoding="utf-8") as f:
            for i, item in enumerate(self.result, start=1):
                for k, v in item.items():
                    line = "filename:" + str(i) + "\t" + k + "\t" + str(v) + "\n"
                    f.write(line)


if __name__ == "__main__":
    P = PreFile()
