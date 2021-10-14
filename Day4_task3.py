# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
def money():
    num = 0
    num1 = len(names)
    age = 0
    #计算每个人平均薪资
    for i in range(num1):
        money = names[i][5]
        num = num + money
    print('每个人平均薪资:',num/num1)

#计算每个人的平均年龄
    for i in range(num1):
        age1 = names[i][1]
        age = age + int(age1)
    print('每个人的平均年龄:',age/num1)

    #添加元素
    names.append(["刘备","45","男","220","alibaba",500,"30"])
    print(names)

    #统计男女个数
    girl = 0
    boy = 0
    for i in range(len(names)):
        if names[i][2] == "男":
            boy += 1
        elif names[i][2] == "女":
            girl += 1
    print(f"男的个数为：{boy},女的个数为:{girl}")

    #每个部门人数
    department = 0
    department1 = 0
    department2 = 0
    department3 = 0
    for i in range(len(names)):
        if names[i][6] == "50":
            department += 1
        elif names[i][6] == "60":
            department1 += 1
        elif names[i][6] == "10":
            department2 += 1
        elif names[i][6] == "30":
            department3 += 1
    print(f"department部门人数为{department},department1部门人数为{department1},department2部门人数为{department2},department3部门人数为{department3}")
money()
#魔法学校
def magic():
    list1 =[
        ["罗恩", 23 ,35 ,44],
        ["哈利" ,60, 77 ,68 ,88, 90],
        ["赫敏", 97 ,99 ,89 ,91, 95, 90],
        ["马尔福" ,100, 85 ,90]
    ]
    for i in range(len(list1)):
        summ = 0
        for j in range(1,len(list1[i])):
            summ = summ + list1[i][j]
        print(list1[i][0],summ)
#方法二
list1 = ["罗恩", 23, 35, 44]
list2 = ["哈利", 60, 77, 68, 88, 90]
list3 = ["赫敏", 97, 99, 89, 91, 95, 90]
list4 = ["马尔福", 100, 85, 90]
sum1 = 0
name = 0
for i in range(len(list1)):
    if i == 0:
        name = list1[0]
    else:
        sum1 = sum1 + int(list1[i])
print(name+"的成绩为:",str(sum1))
sum2 = 0
for i in range(len(list2)):
    if i == 0:
        name = list2[0]
    else:
        sum2 = sum2 + int(list2[i])
print(name+"的成绩成绩为:",str(sum2))
sum3 = 0
for i in range(len(list3)):
    if i == 0:
        name = list3[0]
    else:
        sum3 = sum3 + list3[i]
print(name+"的成绩为:",sum3)
sum4 = 0
for i in range(len(list4)):
    if i == 0:
        name = list4[0]
    else:
        sum4 = sum4 + list4[i]
print(name+"的成绩为:",sum4)

#冒泡排序
def bubbling():
    a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
    for i in range(len(a)):
        for j in range(1,len(a)-i):
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
    print(a)
