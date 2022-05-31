# Generated by Django 4.0.4 on 2022-05-26 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StatusApp', '0003_statusmodel_statuscode'),
        ('OrderApp', '0009_ordermodel_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='StatusApp.statusmodel'),
        ),
    ]
