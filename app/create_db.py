# pip install peewee

from .models import Country, db
from .print_data import print_data


def create_db(obj_list):
    with db:
        db.create_tables([Country])  # создаем таблицу на основе модели Country
        print("[INFO] Table created successfully.")

        try:
            for obj in obj_list:  # наполняем базу данных
                Country(title=obj[0],
                        region=obj[1],
                        population=obj[2],
                        p_of_world=obj[3],
                        date=obj[4],
                        source=obj[5]).save()
        except Exception as ex:
            print(f"[INFO] Data is not valid. {ex}")
        else:
            print(f"[INFO] The data has been successfully loaded into the database.")
            print_data()  # запускаем последний скрипт получения и вывода конечных данных
