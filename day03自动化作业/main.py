
import unittest
from HTMLTestRunner import HTMLTestRunner
tests = unittest.defaultTestLoader.discover(r'D:\测试历程\自动化\day03',pattern='Test*.py')

#创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="HKR登录测试报告",
    description="HKR测试报告",
    verbosity=1,
    stream=open(file="HKR.html", mode="w+", encoding="utf-8")
)
#执行用例
runner.run(tests)