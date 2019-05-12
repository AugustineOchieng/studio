from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField(max_length=100)
    image_url = models.ImageField(upload_to = 'studio/')
    date_posted = models.DateTimeField(default=timezone.now)
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

class location(models.Model):
    place = models.CharField(max_length=30)
    
    def __str__(self):
        return self.place

class category(models.Model):
    category = models.CharField(max_length=30)

class Picture(models.Model):
    picture_name = models.CharField(max_length=30)
    picture_description = models.TextField(max_length=100)
    picture_image = models.ImageField(upload_to='studio/')
    location = models.ManyToManyField(location)
    datep_posted = models.DateTimeField(default=timezone.now)
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture_name

    @classmethod
    def search_by_place(cls,search_term):
        picture_image = cls.objects.filter(title__icontains=search_term)
        return picture_image
