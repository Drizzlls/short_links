# Generated by Django 4.1 on 2022-08-07 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0007_alter_shotrlinks_initiator_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, null=True, verbose_name='Имя агента')),
                ('surname', models.CharField(max_length=75, null=True, verbose_name='Фамилия агента')),
                ('link_agent', models.CharField(blank=True, max_length=195, verbose_name='Ссылка')),
                ('agent_phone', models.CharField(max_length=12, null=True, verbose_name='Номер телефона Агента')),
            ],
            options={
                'verbose_name': 'Агента',
                'verbose_name_plural': 'Агенты',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, null=True, verbose_name='Имя менеджера')),
                ('surname', models.CharField(max_length=75, null=True, verbose_name='Фамилия менеджера')),
                ('agents', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='links.agent')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.AddField(
            model_name='agent',
            name='manager_personal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='links.manager'),
        ),
    ]
