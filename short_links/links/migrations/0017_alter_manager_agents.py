# Generated by Django 4.1.1 on 2022-09-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0016_manager_idfrombitrix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='agents',
            field=models.IntegerField(default=0, verbose_name='Количество агентов'),
        ),
    ]
