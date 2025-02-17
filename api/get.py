from django.shortcuts import render

from django.http import HttpResponse, HttpRequest, JsonResponse

from api.db_conn import save_random_data, get_all_authors

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_data(request: HttpRequest):
    """ получаем из запроса POST функции get_organization_name информацию и переносим её в my_data """
    print(dict(request.POST.items()))
    my_data = dict(request.POST.items())
    save_random_data(my_data)
    return HttpResponse('Данные отправлены')


@csrf_exempt
def get_data(request: HttpRequest):
    all_authors = get_all_authors()
    data = {}
    for author in all_authors:
        data[author.id] = {'name': author.name_author, 'salary': author.salary, 'position': author.position}
    return JsonResponse(data)

# FAstApi и Post запрос
