# Generated by Django 2.2 on 2020-12-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_openningtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
