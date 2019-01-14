from django.urls import path

from . import views

app_name = "monthlycalc"

urlpatterns = [
    path('', views.index, name='monthlycalc'),
]