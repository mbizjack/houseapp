from django.shortcuts import render
from .models import HPI_state,RawHPIform

def place_value(number): 
    return ("{:,}".format(number)) 

def HPIview(request):

	queryset = HPI_state.objects.values("state").distinct()

	form = RawHPIform(request.GET)

	stateChoice = None
	stateQuery = None
	yearlower = None
	yearupper = None
	principal = None
	aprPct = None
	termMo = None
	result = None
	endYr = None
	endValue = None
	endHPI = None
	startHPI = None
	returnPct = None
	endValueCPI = None

	if request.method == 'POST':
		form = RawHPIform(request.POST)
		if form.is_valid():
			stateChoice = form.cleaned_data.get('state')
			yearlower = form.cleaned_data.get('yearlower')
			yearupper = form.cleaned_data.get('yearupper')
			stateQuery = HPI_state.objects.filter(state = stateChoice,
													year__gte = yearlower,
													year__lte = yearupper)
			
			principal = form.cleaned_data.get('principal')
			aprPct = form.cleaned_data.get('apr')/100
			termMo = form.cleaned_data.get('term')*12

			result = (aprPct/12)*principal/(1-((1+aprPct/12)**(-termMo)))

			endYr = yearlower + int((termMo/12))

			startHPI = HPI_state.objects.get(state = stateChoice,
													year = yearlower,
													qtr = 1)

			if endYr > 2018:
				endYr = 2018
				endHPI = HPI_state.objects.get(state = stateChoice,
										year = 2018,
										qtr = 2)
			else:
				endHPI = HPI_state.objects.get(state = stateChoice,
														year = int(endYr),
														qtr = 4)


			endValue = (principal/float(startHPI.hpi))*float(endHPI.hpi)
			endValueCPI = (endValue * (float(startHPI.cpi)/float(endHPI.cpi)))
			returnPct = ((endValueCPI-principal)/principal)*100

	else:
		form = RawHPIform()

	context = {
		"form": form,
		"object_list": queryset,
		"stateChoice": stateChoice,
		"stateQuery": stateQuery,
		"yearlower" : yearlower,
		"yearupper" : yearupper,
        'result': place_value(round(result,2)) if result != None else result,
        'principalInput': place_value(round(principal)) if principal != None else principal,
        'principal' : principal,
        'aprInput': aprPct*100 if aprPct != None else aprPct,
        'termInput': termMo/12 if termMo != None else termMo,
        'endYr': endYr,
        'endValue':place_value(round(endValue)) if endValue != None else endValue,
        'returnPct': place_value(round(returnPct,2)) if returnPct != None else returnPct,
        'startHPI': float(startHPI.hpi) if startHPI != None else startHPI,
        'endValueCPI': place_value(round(endValueCPI))	 if endValueCPI != None else endValueCPI,
        'termCalc': endYr - yearlower if endYr != None else endYr,
        'returnPctAnnual':place_value(round(returnPct/(endYr-yearlower),2)) if returnPct != None else returnPct,
	}

	return render(request, "HPIplot/HPIplot.html", context)
