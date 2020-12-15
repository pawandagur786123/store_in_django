# Generated by Django 2.2 on 2020-12-15 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20201214_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedetails',
            name='gallery',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_images', models.FileField(default=None, null=True, upload_to='media/')),
                ('store_details', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App.Storedetails')),
            ],
        ),
    ]
