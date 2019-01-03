from django.db import models
from django.forms import ModelForm

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

# class HPI_state(models.Model):
# 	state = models.CharField('STATE',max_length=2)
# 	year = models.FloatField('YEAR')
# 	qtr = models.IntegerField('QTR')
# 	hpi = models.FloatField('HPI')

# 	def __float__(self):
# 		#x = self.state+str(self.year)+str(self.qtr)
# 		return self.hpi