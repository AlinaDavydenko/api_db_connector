import requests


def get_response(skip: int, limit: int):
    response = requests.get("http://localhost:8000/authors", params={"skip": skip, "limit": limit})
    if response.status_code == 200:
        return response.json()
    else:
        return f'Ошибка {response.status_code}'

#
# a = get_response(0, 50000)
# print(a)
