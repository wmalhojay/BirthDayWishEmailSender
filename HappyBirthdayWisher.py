import smtplib
from pandas import *
from random import *
from datetime import *

data = read_csv("birthdays.csv")
#print(data)

currentTupple = (datetime.now().month, datetime.now().day)
birthDayDict = {}

for index, row in data.iterrows():
    birthDayDict[row["name"]] = (row["month"], row["day"], row["email"])

for key, value in birthDayDict.items():
    if((value[0], value[1]) == currentTupple):
        birthDayPerson = key
        birthDayPersonEmail = value[2]

with open(f"letter_templates/letter_{randint(1, 3)}.txt") as f:
    letter_content = f.read()
    letter_content = letter_content.replace("[NAME]", birthDayPerson)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="testEmail", password="testPassword")
    connection.send(
        from_addr="testEmail",
        to_addrs=birthDayPersonEmail,
        msg=f"Subject: HBday \n\n {letter_content}"
        
    )
    
