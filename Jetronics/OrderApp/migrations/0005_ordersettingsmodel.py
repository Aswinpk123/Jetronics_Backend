# Generated by Django 4.0.4 on 2022-05-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0004_ordermodel_address_ordermodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=1, max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]
