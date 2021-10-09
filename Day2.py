import random
ran = random.randint(10,90)
num = ran
while True:
    num1 = int(input("请输入第一个数字："))
    if num1 == num:
        print("猜对了")
        break
    elif num1 < num:
        print("猜小了")
    else:
        print("猜大了")