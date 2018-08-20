import redis


r = redis.Redis("127.0.0.1", port=6379, db=0)
while True:
    m = r.get("9527#1")
    if m == None:
        r.set("9527#1", "1")
        print("set success")
    r.set("9527#1", str(int(m)+1))
    print(r.get("9527#1"))
