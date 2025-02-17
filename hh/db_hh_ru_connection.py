# сохранение данных в базу данных, полученных из приложения api
import os
import django
from django.db import connection
from hh.connection_to_api import get_response

# Укажите путь к настройкам вашего проекта
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'  # замените на имя вашего проекта

# Инициализируйте Django
django.setup()

from hh.models import TestAuthor


def save_data_in_database(data_from_api: dict):
    """ сохранение данных из api в базу данных приложения hh """
    # conn = connection['hh_database']

    # задание параметров (взято из модели)
    test_authors = TestAuthor(
        id_author=data_from_api['id'],
        name_authors=data_from_api['author']['name'],
        salary=data_from_api['author']['salary'],
        position=data_from_api['author']['position'],
        year=data_from_api['author']['year'],
        award_name=data_from_api['author']['award_name']
    )

    # сохранение в БД
    test_authors.save(using='hh_database')   # test_authors.save()


# data_from_api_ = get_response(0, 1)
# print(data_from_api_)


def save_to_db_add_params():
    """ добавляем параметры skip и limit, и загружаем в базу данных циклом """
    skip = 0
    limit = 0
    for _ in range(0, 5000001):  # 5 000 001
        limit += 10000
        data_from_api_ = get_response(skip, limit)
        skip += 10000
        if skip >= 5000000:
            return True
        for element_api in data_from_api_:
            save_data_in_database(element_api)


print(save_to_db_add_params())

# TODO
## фильтрация данных для выдачи из базы данных по названиям / именам и прочее
