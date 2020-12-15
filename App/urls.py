from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.allstores, name='allstores'),
    path('add/', views.newstore, name='newstore', ),
    path('add/submit/', views.enterstore, name='submit'),
    path('view/', views.store, name='store')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
