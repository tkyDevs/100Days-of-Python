import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.562672  # Your latitude
MY_LONG = -52.710892  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()


def isOverhead():
    if -5 < MY_LAT - iss_latitude < 5:
        if -5 < MY_LONG - iss_longitude < 5:
            return True
    else:
        return False


def isDark():
    if sunset <= time_now.hour <= sunrise:
        return True
    else:
        return False


def getPass():
    """
    :return: Gmail password from another file.
    """
    with open("../../../test.txt", "r") as file:
        password = file.readline()
    return password


def sendNotification():
    password = getPass()
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="sayoyutky@gmail.com", password=password)
        connection.sendmail(from_addr="sayoyutky@gmail.com", to_addrs="tkyDevs@gmail.com", msg="LOOK UP! ISS IS OVERHEAD!")


while True:
    print(f"{time_now}: CHECKING...")
    if isDark() and isOverhead():
        sendNotification()
    elif not isDark():
        print("Not Dark Yet...")
    time.sleep(3600)
