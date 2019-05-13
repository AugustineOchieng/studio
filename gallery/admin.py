from django.contrib import admin
from .models import Image, Picture,  Photographer, Location, Category

admin.site.register(Image)
admin.site.register(Picture)
admin.site.register(Photographer)
admin.site.register(Location)
admin.site.register(Category)
