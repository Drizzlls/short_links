# Generated by Django 4.1 on 2022-08-07 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0009_delete_shotrlinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_phone',
            field=models.CharField(max_length=12, verbose_name='Номер телефона Агента'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='manager_personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='links.manager'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(max_length=75, verbose_name='Имя агента'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='surname',
            field=models.CharField(max_length=75, verbose_name='Фамилия агента'),
        ),
        migrations.RemoveField(
            model_name='manager',
            name='agents',
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=75, verbose_name='Имя менеджера'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='surname',
            field=models.CharField(max_length=75, verbose_name='Фамилия менеджера'),
        ),
        migrations.AddField(
            model_name='manager',
            name='agents',
            field=models.ManyToManyField(null=True, to='links.agent'),
        ),
    ]
