# Generated by Django 4.1 on 2022-08-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0011_alter_manager_agents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='agents',
        ),
        migrations.AddField(
            model_name='manager',
            name='agents',
            field=models.IntegerField(default=1, verbose_name='Количество агентов'),
            preserve_default=False,
        ),
    ]
