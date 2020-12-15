from __future__ import unicode_literals
from django.db import models
import django.db.models.options as options


TYPE_MONDAY = 0
TYPE_TUESDAY = 1
TYPE_WEDNESDAY = 2
TYPE_THURSDAY = 3
TYPE_FRIDAY = 4
TYPE_SATURDAY = 5
TYPE_SUNDAY = 6


WEEKDAYS = [
    (TYPE_MONDAY, "Monday"),
    (TYPE_TUESDAY, "Tuesday"),
    (TYPE_WEDNESDAY, "Wednesday"),
    (TYPE_THURSDAY, "Thursday"),
    (TYPE_FRIDAY, "Friday"),
    (TYPE_SATURDAY, "Saturday"),
    (TYPE_SUNDAY, "Sunday"),
 ]


class Storedetails(models.Model):
    store_name = models.CharField(db_column='Store_name', max_length=1000, blank=True, null=True) 
    store_description = models.CharField(db_column='Store_description', max_length=1000, blank=True, null=True)
    image = models.ImageField(
                                    upload_to='store_banner_image',
                                    blank=True,
                                    null=True
                                    )
    def __unicode__(self):
        return self.email

class OpenningTime(models.Model):
    stores = models.ForeignKey(Storedetails,related_name='stores', null=True, default=None, on_delete=models.CASCADE)
    weekday = models.PositiveIntegerField(
        choices=WEEKDAYS,blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

class GalleryImage(models.Model):
    store_details = models.ForeignKey(Storedetails, default=None, on_delete=models.CASCADE)
    gallery_images = models.FileField(upload_to = 'media/', null=True, default=None)

    def __str__(self):
        return self.store_details.store_name
