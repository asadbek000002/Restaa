# Generated by Django 4.2.1 on 2023-08-25 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity_drink',
        ),
    ]
