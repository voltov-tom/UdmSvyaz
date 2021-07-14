from django.shortcuts import render

from .forms import ElevatorsForm, ElevatorsFormFind
from .models import Elevators


def index(request):
    def last_adds():
        raw = ''
        try:
            raw = Elevators.objects.raw('SELECT id, ADDRESS, UPDATED_AT, COMMENT '
                                        'FROM MAIN_ELEVATORS '
                                        'ORDER BY UPDATED_AT '
                                        'DESC LIMIT 10')
        except ValueError:
            print('sql_request_error')
        return raw

    data = {'title': 'Последние записи:',
            'last_adds': last_adds()}
    return render(request, 'main/index.html', data)


def addition(request):
    form = ElevatorsForm()
    error = ''
    notice = ''
    if request.method == 'POST':
        form = ElevatorsForm(request.POST)
        if form.is_valid():
            form.save()
            notice = 'Запись успешно добавлена'
        else:
            error = 'Ошибка в вводе данных'

    data = {'addition': 'Добавить запись',
            'form': form,
            'error': error,
            'notice': notice
            }
    return render(request, 'main/addition.html', data)


def getting(request):
    form = ElevatorsFormFind()
    error = ''

    form_find = ''
    if request.method == 'POST':
        form = ElevatorsFormFind(request.POST)
        if form.is_valid():
            address = form.cleaned_data.get("address")
            form_find = Elevators.objects.raw(
                'SELECT id, ADDRESS, COMMUNICATION_TYPE, '
                'STATION_TYPE, COMMENT, UPDATED_AT '
                'FROM MAIN_ELEVATORS '
                f'WHERE ADDRESS LIKE "%%{address}%%" '
                'ORDER BY UPDATED_AT')
            if (print(i) for i in form_find) == '':
                error = 'Такой записи нет'
        else:
            error = print('Ошибка ввода')

    data = {'getting': 'Запросить данные',
            'form': form,
            'error': error,
            'form_find': form_find
            }
    return render(request, 'main/getting.html', data)
