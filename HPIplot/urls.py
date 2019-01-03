from django.urls import path

from . import views

urlpatterns = [
    path('', views.HPIview, name='HPIplot'),
]