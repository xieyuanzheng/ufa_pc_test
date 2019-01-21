import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders


def SendEmail(filename,text):
    # 发送邮件
    sender = '121546683@qq.com'
    # receiver = ['121546683@qq.com','335589815@qq.com']
    to_addr_list = ['4141847@qq.com', '335589815@qq.com','76656630@qq.com']
    #to_addr_list = [ '335589815@qq.com']
    subject = 'python email test'
    smtpserver = 'smtp.qq.com'
    username = '121546683@qq.com'
    password = "lokslgvqyawbbhdd"
    msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')
    # 添加附件
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(filename, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '%s' % 'result.html'))
    email_obj = MIMEMultipart()
    email_obj.attach((MIMEText(text, 'plain', 'utf-8')))
    email_obj.attach(part)
    email_obj['Subject'] = Header(subject, 'utf-8')
    email_obj['From'] = Header(sender, 'utf-8')
    email_obj['To'] = Header(';'.join(to_addr_list), 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, to_addr_list, email_obj.as_string())
    smtp.quit()