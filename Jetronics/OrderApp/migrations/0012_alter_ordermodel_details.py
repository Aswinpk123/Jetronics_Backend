# Generated by Django 4.0.4 on 2022-05-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0011_ordermodel_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='details',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]