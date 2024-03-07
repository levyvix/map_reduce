from datetime import date
import requests

from urllib import request


def get_url(path):
    return request.urlopen(path).read()


def days_between(start, end):
    today = date(*start)
    stop = date(*end)

    while today < stop:
        yield "http://jtwolohan.com/evilblog/" + today.strftime("%m-%d-%Y")
        today = today.replace(day=today.day + 1)


# def get_url(path):
#     response = requests.get(path)

#     if response.status_code == 200:
#         return response.text


for day in days_between((2000, 1, 1), (2001, 1, 31)):
    print(day)
    print(get_url(day))
    break
