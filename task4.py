def dict():
    dict = {"k1":"v2","k2":"v2","k3":"v3"}
    for i in dict:
        #print(i)
        print(dict[i])
    dict["k4"] = "v4"
    print(dict)
dict()

def fruit():
    info = {"苹果":32,"香蕉":22,"葡萄":15.5}
    for i in info:
        name = input("请输入水果名称:")
        print(info[name])
fruit()

# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典
Friuts = {
    "苹果": 12.3,
    "草莓": 4.5,
    "香蕉": 6.3,
    "葡萄": 5.8,
    "橘子": 6.4,
    "樱桃": 15.8
}
info = {
    "小明": {
        "fruits": {
            "苹果": 4, "草莓": 13, "香蕉": 10
        },
    },
    "小刚": {
        "fruits": {
            "葡萄": 19, "橘子": 12, "樱桃": 30
        }
    }
}
for i in info.keys():
    totalPrice = 0
    for j in info[i]["fruits"]:
        price = info[i]["fruits"][j] * (Friuts[j])
        totalPrice += price
    print(i, "的总价为：", totalPrice)
    info[i]["money"] = totalPrice
print(info)


# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
def add(num):
    num3 = {}
    for i in num:
        if i not in num3:
            num3[i]=1
        else:
            num3[i] = num3[i] + 1
    print(num3)
    return num3
dict = {}
dict['name']=1+1
print(dict['name'])

list = [21, 21, 21, 56, 10, 10, 56, 10, 56, 56, 56, 56, 56, 56, 56]
add(list)



lii = [21, 21, 21, 56, 10, 10, 56, 10, 56, 56, 56, 56, 56, 56, 56]
lii2 = []
lii2 = sorted(set(lii),key=lii.index)   #将lii列表除重后，放到新列表lii2中
for i in lii2:
    icount = 0
    for j in lii:
        if i == j :
            icount +=1
    print(f"元素{i}在列表里出现的次数为：{icount}次",end=' ')

# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700, "10"]
]
dict = {}
for i in range(len(names)):
    data = []
    for j in range(1, 7):
        data.append(names[i][j])
    dict[names[i][0]] = data
print(dict)