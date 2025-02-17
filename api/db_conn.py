# сохранение данных в базу данных и извлечение данных
import os
import django

# Укажите путь к настройкам вашего проекта
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'  # замените на имя вашего проекта

# Инициализируйте Django
django.setup()

from api.models import Organization, Author

from api.my_data_generator import generate_my_data


def save_random_data(my_data: dict):
    """ сохраняем данные в базу данных из словаря my_data """
    orgs = Organization(
        name_organization=my_data.get('organization_name'),
    )
    authors = Author(
        name_author=my_data.get('author_name'),
        salary=my_data.get('salary'),
        position=my_data.get('position'),
        year=my_data.get('year'),
        award_name=my_data.get('award_name')
        # organization=my_data.get('organization_name')
    )

    # сохранение в БД
    orgs.save()
    authors.save()


# Создание объекта и сохранение его в базе данных
# for i in range(5000000):
#     my_data_for_bd = generate_my_data()
#     save_random_data(my_data_for_bd)


def get_all_authors(skip: int = 0, limit: int = 10):
    """ вытаскиваем все элементы из БД таблицы Author с пагинацией """
    author = Author.objects.all()[skip: skip + limit]  # Применяем пагинацию
    return author


def get_authors_from_bd():
    data = {}
    all_authors = get_all_authors()
    for author in all_authors:
        data[author.id] = {
            'name': author.name_author,
            'salary': author.salary,
            'position': author.position,
            'year': author.year,
            'award_name': author.award_name
        }
    return data

# a = get_authors_from_bd()
# print(a)

# python manage.py runserver
