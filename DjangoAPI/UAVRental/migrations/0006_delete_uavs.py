# Generated by Django 3.2.19 on 2023-08-11 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UAVRental', '0005_rename_uav_uavs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Uavs',
        ),
    ]
