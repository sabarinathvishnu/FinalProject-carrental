# Generated by Django 5.0.1 on 2024-07-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_bookingdb_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdb',
            name='phonenumber',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
