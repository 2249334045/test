import random
def case_print():
    print("***********************")
    print("*   中国农业银行        *")
    print("***********************")
    print("*     1、开户          *")
    print("*     2、存钱          *")
    print("*     3、取钱          *")
    print("*     4、转账          *")
    print("*     5、查询          *")
    print("*     6、再见          *")
    print("***********************")
index = 0
#空字典
bank={}
#'F': {'account': 98835406, 'password': '1', 'country': '中国', 'porvince': '昌平', 'street': '001', 'door': '001', 'money': 0}
bank_name="中国农业银行昌平支行"
#调用的函数元素是一一对应的，不是名称对应
def bank_add(account,username,password,country,province,street,door):
    if username in  bank:#名字  重名
        return 2
    elif len(bank)>= 100:#大于100个用户
        return 3
    else:#正常添加用户
        bank[username]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
def Useradd():
    account=random.randint(10000000,99999999)#账号随机产生的
    username=input("请输入您的姓名")
    password=input("请输入你的密码")
    print("下面请输入您的地址：")
    country=input("\t\t请输入你的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    add=bank_add(account,username,password,country,province,street,door)
    if add ==3:
        print("数据库已满，请到农业银行开户")
    elif add==2:
        print("用户已存在")
    elif add ==1:
        print("恭喜你添加用户成功，以下是您的账户信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))

#存钱
def save_money():
    account = int(input("请输入存钱账号："))
    pdd = storage(account)
    if pdd:
        print("存钱成功！")
    else:
        print("无此账户")
#判断账户是否存在
def storage(account):
    for username,vlaue1 in bank.items():
        for key,vlaue in vlaue1.items():
            if account == vlaue:
                if index == 2:
                    money = input("请输入存款金额：")
                    vlaue1.update({"money":money})
                return True
    return False

#取钱
def draw_money():
    account = input("请输入您的账号：")
    password = input("请输入您的密码：")
    pdd = draw_money1(account,password)
    if pdd == 3:
        print("账户不存在，未开户")


#转账
def transfer():
    account = input("请输入转入账号：")
    password = input("请输入密码")
    draw_money1(account,password)


#判断取钱账户和密码以及钱数
def draw_money1(account,password):
    for username,vlaue1 in bank.items():
        for key ,vlaue in vlaue1.items():
            if account == vlaue1["account"] and password == vlaue1["password"]:
                print(f"当前余额{vlaue1['money']}")
            if index == 3:
                money = int(input("请输入取款金额："))
                if money > int(vlaue1['money']):
                    print('取款金额大于当前余额，取款失败')
                else:
                    money1 = int(vlaue1['money']) - money
                    vlaue1.update({"money":money1})
                    print("取款成功")
                return 1
            if index == 4:
                account_1 = input("请输入转出账号：")
                pdd = storage(account_1)
                if pdd:
                    money = int(input("请输入转账金额"))
                    if money > int(vlaue1["money"]):
                        print('转账金额大于当前余额，转账失败')
                    else:
                        money1 = int(vlaue1["money"]) - money
                        vlaue1.update({"money":money1})
                        for username2,vlaue2 in bank.items():
                            for key3,vlaue3 in vlaue2.items():
                                if account_1 == vlaue3:
                                    vlaue2.update({"money":money})
                    print("转账成功")
                    return 1
                else:
                    print("转入账户不存在，转账失败")
            else:
                if account == vlaue1['account'] and password != vlaue1['password']:
                    print("密码错误！")
                    return 2
    return 3

#查询
def query():
    account = int(input("请输入账号："))
    password = input("请输入密码：")
    pdd = query_1(account,password)
    if pdd:
        print("账户不存在，未开户")

##判断账户和密码是否正确
def query_1(account,password):
    for username,vlaue1 in bank.items():
        for key,vlaue in vlaue1.items():
            if account == vlaue1['account'] and password == vlaue1['password']:
                print(f"当前账号：{vlaue1['account']},密码:{vlaue1['password']},余额：{vlaue1['money']}元,", end='')
                print(
                    f"用户居住地址：{vlaue1['country'] + vlaue1['province'] + vlaue1['street'] + vlaue1['door']},",
                    end='')
                print(f"当前账户的开户行：{vlaue1['bank_name']}.")
                return False
            else:
                if account == vlaue1['account'] and password != vlaue1['password']:
                    print("密码错误")
                return False
        return True

while True:
    case_print()
    index = int(input("请输入您的操作："))
    if index == 1:
        Useradd()
        print(bank)
    elif index == 2:
        save_money()
    elif index == 3:
        draw_money()
    elif index == 4:
        transfer()
    elif index == 5:
        query()
        break