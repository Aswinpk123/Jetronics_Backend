# Generated by Django 4.0.4 on 2022-05-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0007_alter_ordermodel_product_colour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='product_colour',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='product_size',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]