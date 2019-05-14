from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$', views.home, name='gallery-home'),
    url('^lensflare/', views.lensflare, name='gallery-lensflare'),
    url('^photoboom/', views.photoboom, name='gallery-photoboom'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\d+)',views.location,name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)