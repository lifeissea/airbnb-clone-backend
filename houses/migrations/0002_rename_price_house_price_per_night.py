# Generated by Django 4.1.5 on 2023-01-12 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='price',
            new_name='price_per_night',
        ),
    ]
