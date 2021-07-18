from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import UpdateView, DetailView

from .forms import ElevatorsForm, ElevatorsFormFind
from .models import Elevators


@login_required
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


@login_required
def addition(request):
    message = ''
    form = ElevatorsForm()
    if request.method == 'POST':
        form = ElevatorsForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Адрес успешно добавлен.'
            form = ElevatorsForm(initial={'address': '', 'communication_type': '', 'comment': ''})
        else:
            message = 'Адрес уже существует.'
            form = ElevatorsForm(initial={'address': '', 'communication_type': '', 'comment': ''})
    else:
        pass

    data = {'addition': 'Добавить адрес',
            'form': form,
            'message': message
            }
    return render(request, 'main/addition.html', data)


@login_required
def getting(request):
    form = ElevatorsFormFind()
    form_find = ''
    message = ''
    if request.method == 'POST':
        form = ElevatorsFormFind(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            form = ElevatorsFormFind(initial={'address': ''})
            form_find = Elevators.objects.filter(address__icontains=address).all
        else:
            form = ElevatorsFormFind(initial={'address': ''})
            message = 'Ошибка ввода'
    else:
        pass

    data = {'getting': 'Запросить данные',
            'form': form,
            'form_find': form_find,
            'message': message
            }
    return render(request, 'main/getting.html', data)


class ElevatorsDetailView(LoginRequiredMixin, DetailView):
    model = Elevators
    template_name = 'main/lift.html'
    context_object_name = 'lift'
    redirect_field_name = '/accounts/login/'


class ElevatorsUpdateView(LoginRequiredMixin, UpdateView):
    model = Elevators
    form_class = ElevatorsForm
    template_name = 'main/update.html'
    redirect_field_name = '/accounts/login/'
