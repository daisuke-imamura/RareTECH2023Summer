# Generated by Django 3.2.18 on 2023-08-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antoquinoapp', '0003_auto_20230813_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorire',
        ),
        migrations.AddField(
            model_name='recipe',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
