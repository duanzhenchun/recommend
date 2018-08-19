# 人工干预推荐
import socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(("127.0.0.1", 8888))
# request_data = "空气净化器" + "&" + "1"

request_data = "815439" + "&" + "2"    # 要求返回的结果必需以815439开头
ss.sendall(request_data.encode())
data = ss.recv(1024).decode()
print("server's response: {}".format(data))
ss.close()