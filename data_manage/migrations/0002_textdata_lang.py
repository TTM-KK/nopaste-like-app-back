# Generated by Django 3.2.13 on 2022-06-26 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textdata',
            name='lang',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
