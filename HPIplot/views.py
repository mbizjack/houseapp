from django.shortcuts import render
from .models import HPI_state,RawHPIform


def HPIview(request):

	queryset = HPI_state.objects.values("state").distinct()

	form = RawHPIform(request.GET)

	stateChoice = None
	stateQuery = None
	yearlower = None
	yearupper = None
	if request.method == 'POST':
		form = RawHPIform(request.POST)
		if form.is_valid():
			stateChoice = form.cleaned_data.get('state')
			yearlower = form.cleaned_data.get('yearlower')
			yearupper = form.cleaned_data.get('yearupper')
			stateQuery = HPI_state.objects.filter(state = stateChoice,
													year__gte = yearlower,
													year__lte = yearupper)
	else:
		form = RawHPIform()

	context = {
		"form": form,
		"object_list": queryset,
		"stateChoice": stateChoice,
		"stateQuery": stateQuery,
		"yearlower" : yearlower,
		"yearupper" : yearupper
	}

	return render(request, "HPIplot/HPIplot.html", context)
