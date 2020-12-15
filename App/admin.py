from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from .models import Storedetails, OpenningTime, GalleryImage


class GalleryImageAdmin(admin.TabularInline):
    model = GalleryImage

class StoredetailsAdmin(admin.ModelAdmin):
    model = Storedetails
    inlines = [GalleryImageAdmin]

class OpenningTimeAdmin(ForeignKeyAutocompleteAdmin):
    model = OpenningTime



admin.site.register(Storedetails, StoredetailsAdmin)
admin.site.register(OpenningTime, OpenningTimeAdmin)



# Register your models here.
