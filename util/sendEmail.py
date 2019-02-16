import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders


def SendEmail(listpart,text,to_addr_list):
    # 发送邮件
    sender = '335589815@qq.com'
    # receiver = ['121546683@qq.com','335589815@qq.com']
    #to_addr_core = ['4141847@qq.com', '121546683@qq.com','76656630@qq.com','181643605@qq.com','368422559@qq.com','297086499@qq.com']
    #to_addr_myself = [ '121546683@qq.com']
    subject = 'python email test'
    smtpserver = 'smtp.qq.com'
    username = '335589815@qq.com'
    #password = "lokslgvqyawbbhdd"  #果酱
    password = "mhbabtcaawwebjad"  #今晚打老虎
    msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')
    # 添加附件
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(listpart[0], 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '%s' % 'result.html'))
    email_obj = MIMEMultipart()
    email_obj.attach((MIMEText(text, 'plain', 'utf-8')))
    email_obj.attach(part)
    if os.path.exists(listpart[1]):
        PicturePart = MIMEApplication(open(listpart[1],'rb').read())
        PicturePart.add_header('Content-Disposition', 'attachment', filename='sd12.jpg')
        email_obj.attach(PicturePart)

    email_obj['Subject'] = Header(subject, 'utf-8')
    email_obj['From'] = Header(sender, 'utf-8')
    email_obj['To'] = Header(';'.join(to_addr_list), 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, to_addr_list, email_obj.as_string())
    smtp.quit()