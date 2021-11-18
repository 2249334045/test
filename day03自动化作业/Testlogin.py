import openpyxl
import xlrd
from xlutils.copy import copy
import unittest
from unittest import TestCase
from ddt import ddt,data,unpack
from loginOperation import login_interfacr
from selenium import webdriver
import time
wb = xlrd.open_workbook( r'D:\测试历程\自动化\day03\HKR.xlsx', encoding_override=True)
wblen = len(wb.sheets())
wb_copy = copy(wb)

loginSuccessData = []
loginErrorData = []
for i in range(wblen):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    for j in range(1,rows):
        data = st.row_values(j)
        if i == 0:
            loginSuccessData.append([data[0],data[1],data[2],j])
        if i == 1:
            loginErrorData.append([data[0],data[1],data[2],j])


@ddt
class test_login(TestCase):
    global wb_copy

    # 在所有用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Edge()
        self.driver.get("http://localhost:8081/HKR")
        self.driver.maximize_window()


    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()

        @data(*loginSuccessData)
        @unpack
        def testloginsuccess(self,testdata):
            username = testdata[0]
            password = testdata[1]
            expect = testdata[2]

            login = login_interfacr(self.driver)
            # 执行登陆的三项操作
            login.login1(username, password)

            # 获取实际结果
            result = login.getlogin_successfully()

            time.sleep(3)

            if result == expect:
                wb_copy.get_sheet(0).write(testdata[3], 3, "通过")
                wb_copy.sava('HKR.xls')
            else:
                wb_copy.get_sheet(0).write(testdata[3], 3, "不通过")
                wb_copy.sava('HKR.xls')

            # 断言
            self.assertEqual(expect, result)


        @data(*loginErrorData)
        @unpack
        def testloginerror(self,testdata):
            username = testdata[0]
            password = testdata[1]
            expect = testdata[2]

            login = login_interfacr(self.driver)

            #执行登录的三项操作
            login.login1(username,password)

            #获取实际结果
            result = login.getlogin_failure()
            time.sleep(3)

            if result == expect:
                wb_copy.get_sheet(0).write(testdata[3], 3, "通过")
                wb_copy.sava('HKR.xls')
            else:
                wb_copy.get_sheet(0).write(testdata[3], 3, "不通过")
                wb_copy.sava('HKR.xls')

            # 断言
            self.assertEqual(expect, result)





