


# 多线程内存更新
import threading
from time import ctime, sleep
lock = 0   # 0 表示可以读  # 1 表示可以写

category_items = {}  # category: goods_id


def write():
    print("I'm writing")
    while True:
        print("=============================")
        if lock == 0:
            print("=============================")
            lock = 1
            with open("./logfile.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    ls = line.split("&")
                    if ls[5] not in category_items.keys():
                        category_items[ls[5]] = []
                    category_items[ls[5]].append(ls[4])
            lock = 0
            print("write success.")
        else:
            print("write failed")
            sleep(1)


def read():
    print("I'm reading.")
    while True:
        if lock == 0:
            for k, v in category_items.items():
                print(k + "\t" + "&&".join(v[:5]))
            print("read success.")

        else:
            sleep(1)
            print("read failed.")


threads = []
t1 = threading.Thread(target=write, args=())
threads.append(t1)
t2 = threading.Thread(target=read, args=())
threads.append(t2)

for t in threads:
    t.setDaemon(True)
    t.start()