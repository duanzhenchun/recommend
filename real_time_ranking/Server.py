import socket
import random
import redis

r2 = redis.Redis("127.0.0.1", 6380, db=0)


HOST, PORT = "", 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print("Server HTTP on port {} ......".format(PORT))


class RTR(object):
    old = [1, 2, 3, 4, 5]
    new = [5, 4, 3, 2, 1]

    def __init__(self):
        pass

    def p(self):
        m = r2.get("9527#1")
        print(m)
        if m != None:
            return ",".join([str(i) for i in self.new])
        else:
            return ",".join([str(i) for i in self.old])



while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode()
    paras, tag = request.split("&")[0], int(request.split("&")[1])

    http_response = RTR().p()
    client_connection.sendall(http_response.encode())
    client_connection.close()
