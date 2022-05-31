# Generated by Django 4.0.4 on 2022-05-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0005_testtable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Testtable',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='colour',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='size',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
