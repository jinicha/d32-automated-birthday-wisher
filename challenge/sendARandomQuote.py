# challenge 1: send a random quote on Wednesday

import datetime as dt
import random as rd
import smtplib
# import sys
# import os
# sys.path.append(os.path.dirname(os.getcwd()))

# import config

# gmail = config.gmail
# gmail_pw = config.gmail_pw
# yahoo = config.yahoo


gmail = ""  # sender email
gmail_pw = ""  # sender pw
yahoo = ""  # recipient email

# get current day of the week
now = dt.datetime.now()
current_day = now.weekday() # Wednesday is 2

if current_day == 2:
  # open quotes.txt and obtain a list of quotes
  with open("quotes.txt", "r") as f:
    lines = f.readlines()
    # pick a random quote
    randomQuote = lines[rd.randrange(0, len(lines))]

  # send the random quote email
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=gmail, password=gmail_pw)
    connection.sendmail(
      from_addr=gmail,
      to_addrs=yahoo,
      msg=f"Subject: Wednesday Quote!\n\n{randomQuote}"
    )