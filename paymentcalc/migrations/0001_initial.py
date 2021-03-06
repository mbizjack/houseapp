# Generated by Django 2.1.4 on 2019-01-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HPI_state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=2, verbose_name='STATE')),
                ('year', models.FloatField(verbose_name='YEAR')),
                ('qtr', models.IntegerField(verbose_name='QTR')),
                ('hpi', models.FloatField(verbose_name='HPI')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.FloatField(default=250000.0, verbose_name='Loan Princiapl ($)')),
                ('term', models.FloatField(default=30.0, verbose_name='Loan Term (yr)')),
                ('apr', models.FloatField(default=4.25, verbose_name='Annual Interest Rate (%)')),
            ],
        ),
    ]
