category_items = {} # category: goods_id
with open("./logfile.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        ls = line.split("&")
        if ls[5] not in category_items.keys():
            category_items[ls[5]] = []
        category_items[ls[5]].append(ls[4])

for k, v in category_items.items():
    print(k + "|" + str(len(v)) + "  " + "#".join(v))

with open("cat.txt", "w", encoding="utf-8") as f:
    for k, v in category_items.items():
        f.write(k + "\t" + "&&".join(v))
        f.write("\n")

