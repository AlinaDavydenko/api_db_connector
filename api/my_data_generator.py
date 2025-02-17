# генерирование данных, которые передаются в базу данных
import requests

# from django.views.decorators.csrf import csrf_exempt

import random


from api.data import salaries, author_positions, literary_awards, names


def get_organization_name(data_inf: dict):
    """ Отправка POST-запроса с CSRF-токеном """

    response = requests.post('http://127.0.0.1:8000/organization/', data=data_inf)


def generate_my_data():
    """ генерация данных и добавление в словарик """
    digits = [str(i) for i in range(10)]

    # составление рандомных данных для организации
    name_org = random.choice(names)
    organization_id = random.choice(digits)

    # составление рандомных данных для автора
    name_author = random.choice(names)
    salary = random.choice(salaries)
    position = random.choice(author_positions)
    year = random.choice(digits)
    award_name = random.choice(literary_awards)

    # формирование словаря
    data = {
        'author_name': name_author,
        'salary': salary,
        'position': position,
        'year': year,
        'award_name': award_name,
        'organization_name': name_org,
        'organization_id': organization_id
    }

    return data  # создан словарь с данными


# a = generate_my_data()
# print(a)
