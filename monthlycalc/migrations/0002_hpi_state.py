# Generated by Django 2.1.4 on 2019-01-27 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthlycalc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HPI_state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=2, verbose_name='STATE')),
                ('year', models.IntegerField(verbose_name='YEAR')),
                ('qtr', models.IntegerField(verbose_name='QTR')),
                ('hpi', models.DecimalField(decimal_places=4, max_digits=100, verbose_name='HPI')),
            ],
        ),
    ]
