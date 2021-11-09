import smtplib
import datetime as dt
import random

with open("quotes.txt") as data:
    data = data.readlines()
    quote = random.choice(data)

if dt.datetime.now().weekday() == 0:
    myemail = "codedreamer09@gmail.com"
    password = "12345#aadi"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myemail, password=password)
        connection.sendmail(from_addr=myemail, to_addrs="vaibhav80@gmail.com",
                            msg=f"Subject:Important message by CODE DREAMER\n\n{quote}")
