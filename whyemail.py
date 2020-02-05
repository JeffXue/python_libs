#!/usr/bin/env python3.7

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:

    host = None
    user = None
    password = None

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def send_email(self, html_msg, subject, receivers, cc=None):
        """

        :param html_msg: 邮件主题信息
        :param subject: 邮件标题
        :param receivers: 收件人，以英文逗号为分隔符
        :param cc: 抄送人，以英文逗号为分隔符
        :return:
        """
        msg_root = MIMEMultipart()
        msg_root['From'] = self.user
        msg_root['To'] = receivers
        if cc:
            msg_root['Cc'] = cc
        msg_root["Subject"] = subject

        msg = html_msg
        msg_body = MIMEText(msg, "html", "utf-8")
        msg_root.attach(msg_body)

        smtp = smtplib.SMTP()
        smtp.connect(self.host)
        smtp.login(self.user, self.password)
        if cc:
            smtp.sendmail(self.user, receivers.split(',')+cc.split(','), msg_root.as_string())
        else:
            smtp.sendmail(self.user, receivers.split(','), msg_root.as_string())
        smtp.quit()


if __name__ == '__main__':
    import os
    email_sender = EmailSender(os.environ.get('MAIL_SERVER'),
                               os.environ.get('MAIL_USERNAME'),
                               os.environ.get('MAIL_PASSWORD'))
    email_body = 'email body'
    email_title = 'email title'
    email_sender.send_email(email_body,  email_title, os.environ.get('EMAIL_RECEIVERS'), os.environ.get('EMAIL_CC'))