# Generated by Django 4.2.4 on 2023-08-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uavs',
            fields=[
                ('UavID', models.AutoField(primary_key=True, serialize=False)),
                ('Brand', models.CharField(max_length=50)),
                ('Model', models.CharField(max_length=50)),
                ('Weight', models.IntegerField()),
                ('Image', models.CharField(max_length=50)),
                ('CategoryID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('RentalID', models.AutoField(primary_key=True, serialize=False)),
                ('UavID', models.IntegerField()),
                ('CustomerID', models.IntegerField()),
                ('BeginDate', models.DateTimeField(auto_now=True)),
                ('EndDate', models.DateTimeField(auto_now=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
