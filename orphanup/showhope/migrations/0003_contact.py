# Generated by Django 3.1.6 on 2021-06-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showhope', '0002_auto_20210617_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('ContactID', models.IntegerField(primary_key=True, serialize=False)),
                ('user_Name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Created_date', models.DateField(auto_now_add=True)),
                ('Updated_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
