from HTMLTestRunner import HTMLTestRunner
import unittest

#1.加载所有用例
test = unittest.defaultTestLoader.discover(r"C:\Users\29861\Desktop\python代码\任务\day13",pattern="Test*.py")

#2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器的测试报告",
    description="这是测试报告",
    verbosity=1,
    stream=open(file="计算器.html",mode="w+",encoding="utf-8")
)

#3.执行用例
runner.run(test)

# #4.发送邮件
# import smtplib
# from email.header import Header
# from email.mime.text import MIMEText
#
# #发件人和收件人
# sender = "2249334045@qq.com"
# receiver = "2249334045@qq.com"
#
# #所使用的用来发送邮件的SMTP服务器地址
# smtpserver = "smtp.qq.com"
#
# #发送邮箱的用户名和密码
# username = '2249334045@qq.com'
# password = 'snnyfswcwaejebde'
#
# #邮件主题
# mail_title = '测试报告'
#
# #读取html文件内容
# f = open(r'C:\Users\29861\Desktop\python代码\任务\day13\计算器.html')
# mail_body = f.read()
# f.close()
# #邮件内容，格式，编码
# message = MIMEText(mail_body,'html','utf-8')
# message['From']  = sender
# message['To'] = receiver
# message['Subject'] = Header(mail_title,'utf-8')
#
# try:
#     smtp = smtplib.SMTP()
#     smtp.connect('smtp.qq.com')
#     smtp.login(username,password)
#     smtp.sendmail(sender,receiver,message.as_string())
#     print('发送邮件成功')
#     smtp.quit()
# except smtplib.SMTPException:
#     print('发送邮件失败！！')