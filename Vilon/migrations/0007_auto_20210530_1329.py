# Generated by Django 3.1.5 on 2021-05-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilon', '0006_auto_20210530_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curtain',
            name='type',
            field=models.CharField(choices=[('tefira', 'תפירה'), ('zebra', 'זברה'), ('roma', 'רומאי'), ('van', 'ואניצני')], default='tefira', max_length=30),
        ),
    ]
