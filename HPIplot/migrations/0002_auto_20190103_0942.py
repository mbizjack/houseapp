# Generated by Django 2.1.4 on 2019-01-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HPIplot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hpi_state',
            name='hpi',
            field=models.DecimalField(decimal_places=4, max_digits=100, verbose_name='HPI'),
        ),
        migrations.AlterField(
            model_name='hpi_state',
            name='year',
            field=models.IntegerField(verbose_name='YEAR'),
        ),
    ]
