# Generated by Django 4.0.4 on 2022-05-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StatusApp', '0002_citiesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmodel',
            name='statuscode',
            field=models.CharField(default='', max_length=100),
        ),
    ]
