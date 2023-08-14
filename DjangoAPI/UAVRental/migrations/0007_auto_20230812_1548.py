# Generated by Django 3.2.19 on 2023-08-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UAVRental', '0006_delete_uavs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('BrandID', models.AutoField(primary_key=True, serialize=False)),
                ('BrandName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryID', models.AutoField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('ModelID', models.AutoField(primary_key=True, serialize=False)),
                ('ModelName', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
    ]
