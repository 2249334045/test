from selenium import webdriver
import time
class login_interfacr:
    #定义一个全局变量
    def __init__(self,driver):
        self.driver = driver

    def login1(self,username,password):
        self.driver.find_element_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_xpath('//*[@id="password"]').send_keys(password)
        self.driver.find_element_by_id('submit').click()

    #登录成功结果
    def getlogin_successfully(self):
        return self.driver.title

    #登录失败结果
    def getlogin_failure(self):
        return self.driver.find_element_by_id('msg_uname').text
