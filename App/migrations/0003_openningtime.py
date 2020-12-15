# Generated by Django 2.2 on 2020-12-13 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_delete_openningtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenningTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], unique=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('stores', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='App.Storedetails')),
            ],
        ),
    ]
