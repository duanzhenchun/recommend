
# 多线程内存更新
import threading
from time import sleep


class Lock():
    lock = 0  # 0 表示可以读  # 1 表示可以写
    category_items = {}  # category: goods_id

    def __init__(self):
        with open("./logfile.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                ls = line.split("&")
                if ls[5] not in self.category_items.keys():
                    self.category_items[ls[5]] = []
                self.category_items[ls[5]].append(ls[4])

    def read(self):
        while True:
            if self.lock == 0:
                for k, v in self.category_items.items():
                    print(k + "\t" + "&&".join(v[:5]))
                print("read success.")
            else:
                print("read failed.")
            sleep(1)

    def write(self):
        while True:
            if self.lock == 0:
                self.lock = 1
                with open("./logfile.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        ls = line.split("&")
                        if ls[5] not in self.category_items.keys():
                            self.category_items[ls[5]] = []
                        self.category_items[ls[5]].append(ls[4])
                self.lock = 0
                print("write success.")
            else:
                print("write failed")
            sleep(1)


if __name__ == "__main__":
    l = Lock()
    threads = []
    t1 = threading.Thread(target=l.read, args=())
    threads.append(t1)
    t2 = threading.Thread(target=l.write, args=())
    threads.append(t2)

    for t in threads:
        # t.setDaemon(True)
        t.start()