f = open("day14/baidu_x_system.log", mode="r", encoding="utf-8")
data = f.readlines()
dick ={}
for i in data:
    str = i.split(" ")[0]
    if str not in dick:
        dick[str] = 1
    else:
        dick[str] += 1
print(dick)
