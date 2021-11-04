# pip install pandas

import pandas as pd
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from app.models import Country, db


def print_data():
    def get_region_data(rt):
        with db:
            all_rc = Country.select().where(Country.region == rt).execute()  # получаем все страны региона rt
        r_pop = 0
        min_pop = all_rc[0].population
        min_country = all_rc[0].title
        max_pop = 0
        max_country = ''
        for c in all_rc:
            r_pop += c.population
            if c.population > max_pop:
                max_pop = c.population
                max_country = c.title
            if c.population < min_pop:
                min_pop = c.population
                min_country = c.title
        return {'Region': rt, 'Population': r_pop, 'Max Country': max_country, 'MX Population': max_pop,
                'Min Country': min_country, 'MN Population': min_pop}

    data = []
    unique_rgs = []
    with db:
        for _ in Country.select(Country.region).distinct().order_by(Country.region):  # получаем список всех регионов
            unique_rgs.append(_.region)
        for region in unique_rgs:  # каждый регион пропускаем через get_region_data()
            data.append(get_region_data(region))
    df = pd.DataFrame(data)
    pd.set_option('display.max_columns', None)
    print(df)


# print_data()
