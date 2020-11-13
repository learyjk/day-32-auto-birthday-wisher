# replace email and password below

import pandas
import smtplib
import datetime
from random import randint

birthday_data = pandas.read_csv("birthdays.csv")
birthday_data = birthday_data.to_dict(orient="records")


def send_email(recipient, msg):
    my_email = ""
    password = ""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient,
                            msg=f"Subject:Happy Birthday!\n\n{msg}")


for entry in birthday_data:
    today = datetime.datetime.now()
    if entry['month'] == today.month and entry['day'] == today.day:
        rand = randint(1, 3)
        with open(f"letter_templates/letter_{rand}.txt") as letter:
            msg_to_send = "".join([s for s in letter.readlines()])
            msg_to_send = msg_to_send.replace('[NAME]', entry['name'])
            send_email(recipient=entry['email'], msg=msg_to_send)
