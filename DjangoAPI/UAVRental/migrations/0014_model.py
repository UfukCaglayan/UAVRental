# Generated by Django 3.2.19 on 2023-08-14 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UAVRental', '0013_auto_20230814_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('ModelID', models.AutoField(primary_key=True, serialize=False)),
                ('ModelName', models.CharField(max_length=50)),
                ('BrandID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UAVRental.brand')),
            ],
        ),
    ]
