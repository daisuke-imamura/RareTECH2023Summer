# Generated by Django 3.2.18 on 2023-08-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antoquinoapp', '0004_auto_20230813_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_photos/'),
        ),
    ]
