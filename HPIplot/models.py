from django.db import models

from django import forms

from django.forms.widgets import NumberInput

#from http://abhishekchhibber.com/django-importing-a-csv-file-to-database-models/
# csv migration to database code. run if needed to re-populate database after model migrations
# from HPIplot.models import HPI_state
# import csv
# import os
# path = "C:\\Users\\mbizjack\\Documents\\Python Projects\\House"
# os.chdir(path)
# with open('HPI_AT_state.csv')as csvfile:
#      reader = csv.DictReader(csvfile)
#      for row in reader:
#          p = HPI_state(state = row["STATE"],year = row["YEAR"],qtr = row["QTR"],hpi = row["HPI"])
#          p.save()


class HPI_state(models.Model):
	state = models.CharField('STATE',max_length=2)
	year = models.IntegerField('YEAR')
	qtr = models.IntegerField('QTR')
	hpi = models.DecimalField('HPI',decimal_places=4,max_digits=100)

	def __float__(self):
		x = self.state+str(self.year)+str(self.qtr)
		return x

# class HPIform(forms.ModelForm):
#     class Meta:
#         model = HPI_state
#         fields = ['state']

class RangeInput(NumberInput):
    input_type = 'range'

class RawHPIform(forms.Form):
	state_choices = [(i['state'], i['state']) for i in HPI_state.objects.values('state').distinct()]
	state = forms.ChoiceField(choices=state_choices)
	yearlower = forms.IntegerField(initial=1975,min_value=1975,max_value=2018)
	# Slider widget failure
	#,widget=RangeInput(attrs={'max':2018,'min':1975,'step':1}))
	yearupper = forms.IntegerField(initial=2018,min_value=1975,max_value=2018)
	#,widget=RangeInput(attrs={'max':2018,'min':1975,'step':1}))

