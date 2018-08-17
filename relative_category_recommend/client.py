import socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(("127.0.0.1", 8888))
request_data = "519034" + "&" + "2"
ss.sendall(request_data.encode())
data = ss.recv(1024).decode()
print("server's response: {}".format(data))
ss.close()