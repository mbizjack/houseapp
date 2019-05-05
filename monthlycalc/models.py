from django.db import models
from django.forms import ModelForm,Form
from django import forms


class Input(models.Model):
    principal = models.FloatField(
        verbose_name='Loan Princiapl ($)', default=250000.0)
    term = models.FloatField(
        verbose_name='Loan Term (yr)', default=30.0)
    apr = models.FloatField(
        verbose_name='Annual Interest Rate (%)', default=4.25)

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
