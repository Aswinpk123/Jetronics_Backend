# Generated by Django 4.0.4 on 2022-05-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0002_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='userrandomid',
            field=models.CharField(default='', max_length=255),
        ),
    ]
