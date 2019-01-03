from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from .models import InputForm

import os

def place_value(number): 
    return ("{:,}".format(number)) 
  
def index(request):
#    os.chdir(os.path.dirname(__file__))
    result = None
    aprPct = None
    termMo = None
    principal = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            aprPct = form2.apr/100
            termMo = form2.term*12
            principal = form2.principal
            result = (aprPct/12)*principal/(1-((1+aprPct/12)**(-termMo)))

    else:
        form = InputForm()

    return render(request,'paymentcalc/paymentcalc.html',
            {'form': form,
             'result': place_value(round(result,2)) if result != None else result,
             'principalInput': place_value(round(principal)) if principal != None else principal,
             'aprInput': aprPct*100 if aprPct != None else aprPct,
             'termInput': termMo/12 if termMo != None else termMo,
             })