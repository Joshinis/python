# Generated by Django 3.1.6 on 2021-06-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showhope', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldage',
            name='DOB',
            field=models.CharField(max_length=50),
        ),
    ]
