import random

albet_num = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
user_list = ["one", "two", "three", "four", "five"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
log_type_list = ["1", "2", "3", "4", "5", "6", "7"]
category_list = ["服装", "家居", "食品", "教育", "汽车", "书籍"]


with open("./logfile.txt", "w", encoding="utf-8") as f:
    for i in range(10000):
        cookie = "".join(random.sample(albet_num, 6))
        uid = "".join(random.sample(user_list, 1))
        user_agent = "Macintosh Chorme Safari"
        ip = "192.168.89.177"
        goods_id = "".join(random.sample(num, 6))
        category = "".join(random.sample(category_list, 1))
        order_id = "0"
        log_type = "".join(random.sample(log_type_list, 1))
        final = cookie + "&" + uid + "&" + user_agent + "&" + ip + "&" + goods_id + "&" + category + "&" + order_id + "&" + log_type + "\n"
        f.write(final)
