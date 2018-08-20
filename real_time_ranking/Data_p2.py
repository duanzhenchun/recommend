import redis


r1 = redis.Redis("127.0.0.1", port=6379, db=0)
r2 = redis.Redis("127.0.0.1", port=6380, db=0)
while True:
    m1 = r1.get("9527#1")
    m2 = r2.get("9527#1")
    r2.set("9527#1", m1)
    print(r2.get("9527#1"))
