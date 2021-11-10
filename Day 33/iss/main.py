import requests
from datetime import datetime
import smtplib
import time


while True:
    MY_LAT = 29.058777  # Your latitude
    MY_LONG = 76.085602  # Your longitude

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude, iss_longitude)

    # Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    if time_now >= sunset and time_now <= sunrise and MY_LONG - iss_longitude <= 5 and MY_LAT - iss_latitude <= 5:
        # if time_now >= 17 and time_now >= 5 and MY_LONG - 76 <= 5 and 76 - MY_LONG <= 5:
        myemail = "codedreamer09@gmail.com"
        password = "12345#aadi"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=myemail, password=password)
            connection.sendmail(from_addr=myemail, to_addrs="vaibhav80@gmail.com",
                                msg=f"Subject:ISS is overhead go check\n\n check the sky fast")

    time.sleep(60)
