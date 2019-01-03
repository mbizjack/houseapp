from django.urls import path

from . import views

app_name = "paymentcalc"

urlpatterns = [
	path('',views.index,name='paymentcalculator'),
]