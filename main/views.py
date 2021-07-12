from django.shortcuts import render

from .forms import ElevatorsForm, ElevatorsFormFind
from .models import Elevators


def index(request):
    last_adds = Elevators.objects.raw('SELECT ID, STREET, HOUSE, UPDATED_AT '
                                      'FROM MAIN_ELEVATORS '
                                      'ORDER BY ID DESC LIMIT 10;')
    data = {'title': 'Последние записи:',
            'last_adds': last_adds}
    return render(request, 'main/index.html', data)


def addition(request):
    error = ''
    notice = ''
    if request.method == 'POST':
        form = ElevatorsForm(request.POST)
        if form.is_valid():
            form.save()
            notice = 'Запись успешно добавлена'
        else:
            error = 'Ошибка в вводе данных'

    form = ElevatorsForm()

    data = {'addition': 'Добавить запись',
            'form': form,
            'error': error,
            'notice': notice
            }
    return render(request, 'main/addition.html', data)


def getting(request):
    error = ''
    notice = ''
    form_find = ''
    if request.method == 'POST':
        form = ElevatorsFormFind(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get("city").upper()
            street = form.cleaned_data.get("street").upper()
            house = form.cleaned_data.get("house").upper()
            print(city, street, house)
            form_find = Elevators.objects.raw(
                f"SELECT ID, CITY, STREET, HOUSE, ENTRANCE, ELEVATOR, COMMUNICATION_TYPE, "
                f"STATION_TYPE, COMMENT "
                f"FROM MAIN_ELEVATORS "
                f"WHERE CITY LIKE '%{city}%' and STREET LIKE '%{street}%' and HOUSE LIKE '%{house}%'")
        else:
            error = 'Такой записи нет'
    else:
        error = 'Такой записи нет'

    form = ElevatorsFormFind()

    data = {'getting': 'Запросить данные',
            'form': form,
            'notice': notice,
            'error': error,
            'form_find': form_find
            }
    return render(request, 'main/getting.html', data)
