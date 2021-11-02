'''
    属性：高度，颜色，材质
    行为（方法）：能存放液体
'''

class cup:
    __altitule = 0
    __colour = ""
    __texture = ""

    def setaltitule(self,altitule):
        if altitule < 0 or altitule > 2:
            print("是给人喝的吗？")
        else:
            self.__altitule = altitule
    def getaltitude(self):
        return self.__altitule

    def setcolour(self,colour):
        if colour != "绿色" or colour != "黄色" or colour != "粉色" or colour != "蓝色" or colour != "白色":
            print("没有这种颜色")
        else:
            self.__colour = colour
    def getcolour(self):
        return self.__colour

    def settexture(self,texture):
        self.__texture = texture
    def gettexture(self):
        return self.__texture
c = cup()

'''
    属性：屏幕大小，价格，cpu型号，内存大小，待机时长
    行为（方法）：打字，打游戏，看视频

'''

class backbook:
    __screen = 0
    __price = 0
    __cpu = ""
    __memory = 0
    __stand_by_time = 0

    def setscreen(self,screen):
        if screen <6 or screen > 22:
            print("没有该尺寸的电脑")
        else:
            self.__screen = screen
    def getscreen(self):
        return self.__screen

    def setprice(self,price):
        if price < 0:
            print("颜值刷脸")
        else:
            self.__price = price
    def getprice(self):
        return self.__price

    def setcpu(self,cpu):
        self.__cpu = cpu
    def getcpu(self):
        return self.__cpu

    def setmemory(self,memory):
        if memory < 0:
            print("怎么用？")
        else:
            self.__memory = memory
    def getmemory(self):
        return self.__memory

    def setstand_by_time(self,stand_by_time):
        if stand_by_time <= 0:
            print("苹果牌的？")
        else:
            self.__stand_by_time = stand_by_time
    def getstand_by_time(self):
        return self.__stand_by_time

    def write(self,brand):
        print("亮哥正在用价值",self.__price,"万元的",brand,"牌电脑打字")

    def playgame(self,gamename):
        print("亮哥打",gamename,"的电脑屏幕尺寸是",self.__screen,"英寸")

    def watchvideo(self,video):
        print("亮哥用待机时长",self.__stand_by_time,"小时的电脑看完了",video)


backbook = backbook()

backbook.setscreen(15)
backbook.setprice(20000)
backbook.setcpu("64位")
backbook.setmemory(8)
backbook.setstand_by_time(4)

backbook.write("惠普")
backbook.playgame("英雄联盟")
backbook.watchvideo("长津湖")