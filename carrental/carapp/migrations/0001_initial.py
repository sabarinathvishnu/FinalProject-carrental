# Generated by Django 5.0.4 on 2024-07-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carname', models.CharField(blank=True, max_length=100, null=True)),
                ('brandname', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('vehicletype', models.CharField(blank=True, max_length=100, null=True)),
                ('pickuptime', models.TimeField(blank=True, max_length=100, null=True)),
                ('pickofftime', models.TimeField(blank=True, max_length=100, null=True)),
                ('pickuplocation', models.CharField(blank=True, max_length=100, null=True)),
                ('dropofflocation', models.CharField(blank=True, max_length=100, null=True)),
                ('pickupdate', models.DateField(blank=True, max_length=100, null=True)),
                ('dropoffdate', models.DateField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='signupdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('emailaddress', models.EmailField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('confirmpassword', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
