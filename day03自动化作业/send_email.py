import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#发件人和收件人
sender = "2249334045@qq.com"
receiver = "2249334045@qq.com"   #2431320433

#所使用的用来发送邮件的SMTP服务器地址
smtpserver = "smtp.qq.com"

#发送邮箱的用户名和密码
username = '2249334045@qq.com'
password = 'snnyfswcwaejebde'
message = MIMEMultipart()
#邮件主题
mail_title = MIMEText('测试报告')
message.attach(mail_title)
#附件
mail_application=MIMEApplication(open(r'D:\测试历程\自动化\day03\HKR.html','rb').read())
mail_application.add_header('Content-Disposition','attachment',filename='测试报告.html')
message.attach(mail_application)


#读取html文件内容
# f = open(r'C:\Users\29861\Desktop\python代码\任务\day13\计算器.html','rb')
# mail_body = f.read()
# f.close()
#邮件内容，格式，编码
# message = MIMEText(mail_body,'html','utf-8')
message['From']= sender
message['To'] = receiver
message['Subject'] = Header('测试报告','utf-8')

try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,message.as_string())
    print('发送邮件成功')
    smtp.quit()
except smtplib.SMTPException:
    print("发送邮件失败！！")