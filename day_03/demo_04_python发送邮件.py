# coding=utf-8

import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtp = smtplib.SMTP_SSL("smtp.qq.com", 465) # 初始化服务器连接对象
smtp.login("1546596867@qq.com", "tbmuihepcaxkiefb") # 登录QQ邮箱

msg = MIMEText("我是内容") # 初始化一个文本邮件对象
msg['subject'] = Header("我是标题", 'utf-8') # 给邮件加上标题
msg['From'] = Header("1546596867@qq.com", 'utf-8') # 显示在邮件中的发件人名称
msg['To'] = Header(str(["824966904@qq.com", "2496512114@qq.com", "79798380@qq.com"]), 'utf-8') # 显示在邮件中的收件人名称
print(msg)
smtp.sendmail("1546596867@qq.com", ["824966904@qq.com", "2496512114@qq.com", "79798380@qq.com"], msg.as_string())
smtp.close()