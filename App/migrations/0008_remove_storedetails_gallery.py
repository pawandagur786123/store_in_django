# Generated by Django 2.2 on 2020-12-15 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20201215_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storedetails',
            name='gallery',
        ),
    ]
