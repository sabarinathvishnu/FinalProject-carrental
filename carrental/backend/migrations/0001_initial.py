# Generated by Django 5.0.4 on 2024-07-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoryDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(blank=True, max_length=100, null=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='categoryimages')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleName', models.CharField(blank=True, max_length=100, null=True)),
                ('BrandName', models.CharField(blank=True, max_length=100, null=True)),
                ('VehicleType', models.CharField(blank=True, max_length=100, null=True)),
                ('VehiclePrice', models.IntegerField(blank=True, null=True)),
                ('VehicleImage', models.ImageField(blank=True, null=True, upload_to='categoryimages')),
                ('Enginecapacity', models.CharField(blank=True, max_length=100, null=True)),
                ('Mileage', models.CharField(blank=True, max_length=100, null=True)),
                ('Fuelcapacity', models.CharField(blank=True, max_length=100, null=True)),
                ('Maxpower', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
