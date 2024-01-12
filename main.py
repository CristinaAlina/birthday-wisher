import pandas
import datetime as dt
from random import randint
import smtplib

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR PASS"  # Use Google/Yahoo option for setting specific App password

now = dt.datetime.now()
today_tuple = (now.month, now.day)

birthdays_data = pandas.read_csv("birthdays.csv")
list_birthdays_data = birthdays_data.to_dict(orient="records")  # get a list of dictionaries data

for birthday_person in list_birthdays_data:
    if (birthday_person["month"], birthday_person["day"]) == today_tuple:
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter:
            content = letter.read().replace("[NAME]", birthday_person["name"])

        # For host argument use the specific email provider that you have
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                to_addrs=birthday_person["email"],
                from_addr=MY_EMAIL,
                msg=f"Subject:Happy Birthday!\n\n{content}"
            )
