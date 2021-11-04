# pip install beautifulsoup4 lxml
# pip install psycopg2-binary

import requests
import urllib.request
from bs4 import BeautifulSoup
import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from app.create_db import create_db


url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'


def get_data():
    if requests.get(url).status_code != 200:
        raise Exception(f"unable to connect to source {url}")
    else:
        src = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(src, "lxml")
        t_body = soup.find("table", {"class": "wikitable sortable"}).find("tbody")
        trs = t_body.find_all("tr")
        objs = []  # список объектов стран
        for item in trs[2:]:  # [2:] - первая строка - название столбцов, исключаем её
            tds = item.find_all("td")
            obj_attrs = []  # набираем список атрибутов для будущего объекта Country
            for td in tds:
                obj_attrs.append(td.text.strip())  # в цикле перебираем поля строки, создавая список атрибутов объекта
            obj_attrs[2] = int(obj_attrs[2].replace(',', ''))  # преобразуем str в int, удаляя запятые из строки
            obj_attrs[3] = float(obj_attrs[3].strip('%'))  # преобразуем str в float, удаляя символ "%"
            objs.append(obj_attrs)  # добавляем объект в список объектов
        create_db(objs)  # запускаем скрипт подключения к бд, передаем список объектов


if __name__ == "__main__":
    get_data()
