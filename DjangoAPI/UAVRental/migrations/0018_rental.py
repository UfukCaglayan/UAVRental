# Generated by Django 3.2.19 on 2023-08-14 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UAVRental', '0017_delete_rental'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('RentalID', models.AutoField(primary_key=True, serialize=False)),
                ('CustomerID', models.IntegerField()),
                ('BeginDate', models.DateTimeField()),
                ('EndDate', models.DateTimeField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('UavID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UAVRental.uav')),
            ],
        ),
    ]