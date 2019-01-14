# Generated by Django 2.1.4 on 2019-01-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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