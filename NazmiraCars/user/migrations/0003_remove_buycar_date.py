# Generated by Django 5.0.2 on 2024-03-28 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_buycar_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buycar',
            name='date',
        ),
    ]
