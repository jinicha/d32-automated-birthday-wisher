##################### Normal Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

import datetime as dt
import pandas as pd
import smtplib
import config
import os
import random

# get current month and day
now = dt.datetime.now()
month = now.month
day = now.day

# read data from csv file
data = pd.read_csv("birthdays.csv")
row = data[data.month == month]
if len(row) > 0:
    data_day = row.day
    if data_day.item() == day:
        name = row.name.item()
        email = row.email.item()
        letter = random.choice(os.listdir("letter_templates"))
        with open("letter_templates/" + letter, "r") as f:
            filedata = f.read()
            filedata = filedata.replace("[NAME]", name)
            with open("letter_templates/" + letter, "w") as f:
                f.write(filedata)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=config.gmail, password=config.gmail_pw)
                connection.sendmail(
                    from_addr=config.gmail,
                    to_addrs=email,
                    msg=f'Subject: Happy Birthday!\n\n{filedata}'
                )


