from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addition', views.addition, name='addition'),
    path('getting', views.getting, name='getting'),
    path('main/<pk>/', views.ElevatorsDetailView.as_view(), name='lift'),
    path('main/<pk>/update', views.ElevatorsUpdateView.as_view(), name='update')
]
