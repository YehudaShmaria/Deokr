# Generated by Django 3.1.5 on 2021-06-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilon', '0007_auto_20210530_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curtain',
            name='name',
            field=models.CharField(default='Vilon', max_length=30),
        ),
    ]
