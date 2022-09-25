# Generated by Django 4.0.2 on 2022-02-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shotrlinks',
            old_name='initiator_agent',
            new_name='initiator_phone',
        ),
        migrations.AddField(
            model_name='shotrlinks',
            name='link',
            field=models.CharField(default=1, max_length=195, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]
