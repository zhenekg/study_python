# ver 1.0
import geocoder
import requests
from bs4 import BeautifulSoup


DAYS = [
            {"num" : 0, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [0,1,2,3,4,5,6], "temp" : 0, "type" : "-"},
            {"num" : 1, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [1,2,3,4,5,6,0], "temp" : 0, "type" : "-"},
            {"num" : 2, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [2,3,4,5,6,0,1], "temp" : 0, "type" : "-"},
            {"num" : 3, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [3,4,5,6,0,1,2], "temp" : 0, "type" : "-"},
            {"num" : 4, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [4,5,6,0,1,2,3], "temp" : 0, "type" : "-"},
            {"num" : 5, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [5,6,0,1,2,3,4], "temp" : 0, "type" : "-"},
            {"num" : 6, "title" : "понедельник", "active" : False, "color" : "#FFE739", "order" : [6,0,1,2,3,4,5], "temp" : 0, "type" : "-"}
]


def parse():
    g = geocoder.ip('me')
    city = g.city

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    # US english
    LANGUAGE = "en-US,en;q=0.5"

    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get("https://yandex.ru/pogoda/"+city)

    soup = BeautifulSoup(requests.get(html.text, "html.parser").content)

    print(soup)


def today():
    g = geocoder.ip('me')
    res = {
        "city" : g.city,
        "lat"  : "g.latlng",
        "lng"  : "g.latlng",
        "temp" : 10
    }

    return res
