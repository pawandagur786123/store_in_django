# Generated by Django 2.2 on 2020-12-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20201214_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openningtime',
            name='weekday',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], null=True),
        ),
    ]
