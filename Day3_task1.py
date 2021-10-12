#输入数字求和
def sum():
    N = input("请输入十个数字：")
    t = list(N)
    r = 0
    for i in t:
        r = r + eval(i)
    print(r)

#最大值与最小值
def max_min():
    n = 11
    maxx = 0
    minn = 0
    for i in range(1,n):
        num = int(input(f"请输入第{i}个整数>>"))
        if i == 1:
            minn = num
            # maxx = num
        if maxx < num:
            maxx =num
        # if num < minn:
        if minn > num:
            minn = num
        if minn > num:
            minn = num

    print("十次输入获取的数字中,最大值为{},最小值为{}".format(maxx,minn))
max_min()
#十个数的最小值与最大值并打印
def max_min_average_sum():
    n = 11
    min = 0
    max = 0
    zong = 0
    for i in range(1,n):
        summ = int(input(f"请输入第{i}个数："))
        zong = zong + summ
        if i == 1:
            min = summ
            max = summ
        if max < summ:
            max = summ
        if min > summ:
            min = summ
    print(f"十次输入获取的数字总和为{zong}")
    print(f"十次输入获取的数字中,最大值为{max},最小值为{min}")
    print(f"十次输入获取的数字平均值为{zong/10}")

#使用random模块，如何产生 50~150之间的数
def rand():
    import random
    sun = random.randint(50,150)
    print(sun)

#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
def sjx():
    a1 = int(input("请输入边长："))
    a2 = int(input("请输入边长："))
    a3 = int(input("请输入边长："))
    print(a1,a2,a3)
    if (a1+a2)>a3 or (a1+a3)>a2 or (a2+a3)>a1:
        print("可以形成三角形")
        if a1 == a2 == a3:
            print("可以构成等边三角形")
        if a1 == a2 or a2 == a3 or a1 == a3:
            print("可以构成等腰三角形")
        if a1*a1 + a2*a2 == a3*a3 or a1*a1 + a3*a3 == a2*a2 or a2*a2 + a3*a3 == a1*a1:
            print("可以构成三角形")
    else:
        print("无法构成三角形")
    list1 = [1,2,3,4]
    return list1

def exchange():
    a = 56
    b = 78
    c = b - a
    a = a + c
    b = b - c
    print(a,b)

#登录系统
def login():
    username = "root"
    password = "admin"
    for i in range(3):
        user = input("请输入账号：")
        passwd = input("请输入密码：")
        if user == username and passwd == password:
            print("登录系统成功！")
            break
        elif i == 2:
            print(f"对不起您输入密码错误次数已达{i+1}次")
        else:
            print("账号密码输入错误！")
#打印三角形
def sjx_pattern():
    for i in range(8):
        print(" "*(8-i),"* "* i)

#九九乘法表
def nine():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(f"{j}*{i}={j*i}",end=" | ")
            j = j+1
        print(" ")
        i = i+1

#处罚
def punish():
    import random
    list=["喜羊羊","美羊羊","懒洋洋","暖羊羊","沸羊羊","灰太狼"]
    print("==============欢迎来到处罚系统=================")
    while True:
        index = input("请输入1开始选人：,输入2选择处罚遍数：,输入q或者Q查看处罚结果")
        if index == '1':
            ran = random.choice(list)
        elif index == '2':
            num = random.randint(0,90)
        elif index == 'q' or index == 'Q':
            break
    print(f"{ran}被处罚了{num}遍")

#青蛙
def frog():
    frog_climb =0   # 总爬行
    day = 0         # 多少天g
    while frog_climb < 20:
        frog_climb += 3
        if frog_climb < 20:
            frog_climb += -2
            day += 1
        else:
            day += 1
            print('青蛙用了', day, '天爬了出来')
    else:
        print('走完while循环之后必走这里')

#猜数字
import random
import time
ran = random.randint(0,100)
#print(ran)
def guess_the_num():
    num = ran
    day = 1
    while day < 4:
        num1 = int(input("请输入0~100的整数："))
        if num1 == num:
            print("猜对了")
            print(f"第{day}次猜对奖励1金币")
            break
        elif num1 <num and num1 >= 0:
            print("猜小了")
            day = day + 1
            print("还有",4 - day,"次机会\n",)
        elif num1 > num and num1 <= 100:
            print("大了")
            day = day + 1
            print("还有",4 - day,"次机会\n")
        else:
            print("输入错误")
            day = day + 1
            print("还有",4 - day,"次机会\n")
        if day == 4:
            print("次数已用完，请等待十秒继续猜！")
            time.sleep(10)
            day = 1