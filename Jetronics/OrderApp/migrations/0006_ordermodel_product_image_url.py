# Generated by Django 4.0.4 on 2022-05-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0005_ordersettingsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='product_image_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
