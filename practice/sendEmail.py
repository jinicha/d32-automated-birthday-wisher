import smtplib
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))

import config

gmail = config.gmail
gmail_pw = config.gmail_pw
yahoo = config.yahoo
yahoo_pw = config.yahoo_pw

# from gmail to yahoo
with smtplib.SMTP("smtp.gmail.com") as connection:
  connection.starttls()
  connection.login(user=gmail, password=gmail_pw)
  connection.sendmail(
    from_addr=gmail,
    to_addrs=yahoo,
    msg="Subject: test1\n\nThis is test1 body."
  )

# from yahoo to gmail
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
  connection.starttls()
  connection.login(user=yahoo, password=yahoo_pw)
  connection.sendmail(
    from_addr=yahoo,
    to_addrs=gmail,
    msg="Subject: test2\n\nThis is test2 body."
  )