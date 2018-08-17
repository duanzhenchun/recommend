import random
"""
		点击      1
		播放      2
		点赞      3
		收藏      4
		付费观看   5
		站外分享   6
		评论       7
"""

albet_num = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
user_list = ["one", "two", "three", "four", "five"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
log_type_list = ["1", "2", "3", "4", "5", "6", "7"]
topic_list = ["空气净化器", "净水器", "加湿器", "空气净化滤芯"]


with open("./logfile.txt", "w", encoding="utf-8") as f:
    for i in range(10000):
        cookie = "".join(random.sample(albet_num, 6))
        uid = "".join(random.sample(user_list, 1))
        user_agent = "Macintosh Chorme Safari"
        ip = "192.168.89.177"
        goods_id = "".join(random.sample(num, 6))
        topic = "".join(random.sample(topic_list, 1))
        order_id = "0"
        log_type = "".join(random.sample(log_type_list, 1))
        final = cookie + "&" + uid + "&" + user_agent + "&" + ip + "&" + goods_id + "&" + topic + "&" + order_id + "&" + log_type + "\n"
        f.write(final)
