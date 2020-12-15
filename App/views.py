from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template import Context, loader
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from App.models import *
from django.db import connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import datetime
import json
import urllib, re
import hashlib

def allstores(request):
	allstores = (Storedetails.objects.values('id','store_name','store_description','image'))
	return render(request, "allstores.html", {"stores":allstores, 'media_root': settings.MEDIA_ROOT, 'media_url': settings.MEDIA_URL})

@csrf_exempt
def enterstore(request):
	if request.POST:
		store_name = request.POST.get('newstoreinput')
		store_description = request.POST.get('description')
		cover_pic = request.FILES.get('cover_pic')
		gallery = request.FILES.getlist('gallery_pics')
		fs = FileSystemStorage()
		filename = fs.save(cover_pic.name, cover_pic)
		store_details = Storedetails(store_name = store_name, store_description = store_description)
		store_details.image = filename
		store_details.save()

		try:
			for gal in gallery:
				new_file_storage = None
				gallery_image = fs.save(gal.name, gal)
				galleryimage = GalleryImage(gallery_images = gallery_image, store_details = store_details)
				galleryimage.save()
		except Exception as e:			
			print("Trying to save galleryimage but error at : " + str(e))
			pass
		
		try:
			start_time = request.POST.getlist('startTime')
			if isinstance(start_time, list):
				print("start_time is instance of list")
				pass
			else:			
				start_time = json.dumps(start_time)
				start_time = json.loads(start_time)

			endtime = request.POST.getlist('endTime') 
			end_time = None
			
			if isinstance(end_time, list):
				print("end_time is instance of list")
				pass
			else:			
				end_time = json.dumps(endtime)
				end_time = json.loads(end_time)
				end_time = end_time
			
			for idx,time in enumerate(start_time):
				start_time = datetime.datetime.strptime(time,'%H:%M').time()
				if store_details:
					openning_time,_ = OpenningTime.objects.get_or_create(stores=store_details, weekday = idx, start_time = start_time, end_time = datetime.datetime.strptime(end_time[idx],'%H:%M').time())
		except Exception as e:
			print("Trying to save start and endtime but error at : " + str(e))
			pass
	return render(request,'enterstore.html',{})

def newstore(request):
	return render(request,"newstore.html")

def store(request):
	storeid = request.GET.get('store')
	datas = Storedetails.objects.filter(id=storeid).values('store_name','store_description','image')
	alldata = list(datas)
	data2 = alldata[0]
	name = data2['store_name']
	description = data2["store_description"]
	image = data2["image"]
	gallery = GalleryImage.objects.filter(store_details__id=storeid)
	galleryimage = []
	for gal in gallery:
		galleryimage.append(gal.gallery_images.url)
	weekdays = OpenningTime.objects.filter(stores__id = storeid).order_by('weekday')
	day_arr = []
	for day in weekdays:
		day_arr.append({"day":WEEKDAYS[day.weekday][1],"start_time":day.start_time.strftime('%I:%M %p'), "end_time":day.end_time.strftime('%I:%M %p')})
	return render(request,'store.html',{"name":name,"description":description,"image":image, 'media_root': settings.MEDIA_ROOT, 'media_url': settings.MEDIA_URL, 'day_arr': day_arr, "galleryimage" : galleryimage})



