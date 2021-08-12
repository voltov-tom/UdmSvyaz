from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import UpdateView, DetailView

from .forms import ElevatorsForm
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

    data = {'last_adds': last_adds()}
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

    data = {'form': form,
            'message': message
            }
    return render(request, 'main/addition.html', data)


@login_required
def getting(request):
    if request.method == "POST":
        query_name = request.POST.get('address', None)
        if query_name != '':
            results = Elevators.objects.filter(address__icontains=query_name)
            return render(request, 'main/getting.html', {"results": results})
        else:
            return render(request, 'main/getting.html', {"error": 'Ничего не найдено...'})
    return render(request, 'main/getting.html')


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
