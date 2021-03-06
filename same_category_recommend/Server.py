import socket
import random

HOST, PORT = "", 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print("Server HTTP on port {} ......".format(PORT))

cat_items = {}  # category: goods_id_list
with open("./cat.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        ls = line.split("\t")
        if ls[0] not in cat_items.keys():
            cat_items[ls[0]] = []
        cat_items[ls[0]].extend(ls[1].split("&&"))


def log_process(paras, tag):
    # tag =1 文字 返回与文字匹配的商品
    # tag =2 数字 返回数字同类的商品
    print(paras)
    if tag == 1:
        if paras in cat_items.keys():
            return "&&".join(cat_items[paras])
        else:
            return "wrong paras"

    elif tag == 2:
        for k, v in cat_items.items():
            if paras in v:
                return "&&".join(v)
        return "wrong paras"

    else:
        return "wrong"


while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode()
    paras, tag = request.split("&")[0], int(request.split("&")[1])
    http_response = log_process(paras=paras, tag=tag)
    client_connection.sendall(http_response.encode())
    client_connection.close()
