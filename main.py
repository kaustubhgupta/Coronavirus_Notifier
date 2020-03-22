from plyer import notification
from bs4 import BeautifulSoup
import requests
import time
url = 'https://www.mohfw.gov.in/'


def notifyUser(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "coronavirus.ico",
        timeout = 10
    )


def getData(url):
    r = requests.get(url)
    return r.text
# notifyUser("Hello", 'testing 134 3')

while True:
    htmlForm = getData(url)
    finalCode = BeautifulSoup(htmlForm, 'html.parser')
    # print(finalCode.prettify())
    new = finalCode.find_all('tbody')[1]
    new2 = ''
    new2 += new.get_text()
    new2 = new2[1:]
    new3 = new2.split("\n\n")
    states = ['Haryana', 'Delhi', 'Kerala']
    for i in new3[0:22]:
        dataList = i.split('\n')
        if dataList[2] in states:
            print(dataList)
            titleToBeSent = 'Current Cases of Covid-19'
            nMainText = f"{dataList[2]}: Indian {dataList[3]} Foreign: {dataList[4]} Cured: {dataList[5]} Deaths: {dataList[6]}"
            notifyUser(titleToBeSent, nMainText)
            time.sleep(2)
    time.sleep(3600)
