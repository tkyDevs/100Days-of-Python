import requests
from dotenv import load_dotenv
import os
import datetime
import smtplib
load_dotenv('.project_config')
STOCK = "TSLA"
COMPANY_NAME = "Tesla"


def checkStock():
    yesterdayDate = str(datetime.datetime.now() - datetime.timedelta(1))[0:10]
    dayBeforeYesterdayDate = str(datetime.datetime.now() - datetime.timedelta(2))[0:10]

    myParams = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": os.getenv("stockApi")
    }
    response = requests.get("https://www.alphavantage.co/query", params=myParams)
    data = response.json()

    yesterdayClose = float(data['Time Series (Daily)'][yesterdayDate]['4. close'])
    dayBeforeYesterdayClose = float(data['Time Series (Daily)'][dayBeforeYesterdayDate]['4. close'])
    delta = ((yesterdayClose / dayBeforeYesterdayClose) * 100) - 100
    if delta < -5 or delta > 5:
        sendEmail(delta)
    else:
        print(f"Now news yet! Delta: {delta}")


def getNews():
    myParams = {
        "q": COMPANY_NAME,
        "apikey": os.getenv("newsApi"),
        "sortBy": "publishedAt",
        "pageSize": 3
    }
    response = requests.get("https://newsapi.org/v2/everything", params=myParams)
    data = response.json()
    return data['articles']


def sendEmail(delta):
    if delta > 5:
        sign = "🔺"
    else:
        sign = "🔻"
    news = getNews()
    message = f"""
    {STOCK}: {sign}{delta}%
    
    3 {STOCK} Headlines:
    
    """
    for i in news:
        message += i["description"] + "\n\n"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="tkyDevs@gmail.com", password=os.getenv("gmailPass"))
        connection.sendmail(from_addr="tkyDevs@gmail.com", to_addrs="sayoyutky@gmail.com", msg=message)


checkStock()
