# Generated by Django 2.0.1 on 2018-02-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getdata', '0002_auto_20180217_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='population',
            name='census_tract',
            field=models.FloatField(default=0.0),
        ),
    ]
