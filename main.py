import pandas
import smtplib
import datetime as dt
import random
import os

##################### Extra Hard Starting Project ######################

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

birthdays = pandas.read_csv("birthdays.csv")
birthdays = birthdays.dropna()

today = dt.datetime.today()
today_tuple = (today.month, today.day)

for index, row in birthdays.iterrows():
    birthday_tuple = (int(row["month"]), int(row["day"]))

    if birthday_tuple == today_tuple:
        print("Birthday found")

        name = row["name"]
        email = row["email"]

        random_number = random.randint(1, 3)

        with open(f"letter_templates/letter_{random_number}.txt", "r", encoding="utf-8") as letter_file:
            letter = letter_file.read()

        personal_letter = letter.replace("[NAME]", name)

        print(personal_letter)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday\n\n{personal_letter}"
            )

        print(f"Birthday email sent to {email}")
