# Generated by Django 5.0.1 on 2024-07-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_alter_bookingdb_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdb',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
    ]
