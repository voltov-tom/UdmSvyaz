from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addition', views.addition, name='addition'),
    path('getting', views.getting, name='getting')
]
