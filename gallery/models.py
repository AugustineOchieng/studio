from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location


    def save_location(self):
        self.save()

    def display_location(self):
        return self.location

    def delete_location(self):
        Location.objects.all().delete()

class Category(models.Model):
    category = models.CharField(max_length = 30)


    @classmethod
    def get_categories(cls):
        category = cls.objects.all()
        return category

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def display_category(self):
        return self.category

    def delete_category(self):
        Category.objects.all().delete()



class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_photographer(self):
        self.save()

    def display_photographer(self):
        return self.first_name

    def delete_photographer(self):
        Photographer.objects.all().delete()


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField(max_length=100)
    image_url = models.ImageField(upload_to = 'studio/')
    date_posted = models.DateTimeField(default=timezone.now)
    photographer = models.ForeignKey(Photographer)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def display_image(self):
        return self.image_name

    def delete_image(self):
        Image.objects.all().delete()

    @classmethod
    def get_images(cls):
        image_url = cls.objects.all()
        return image_url

    @classmethod
    def search_by_category(cls,search_term):
        image_url = cls.objects.filter(category__icontains = search_term)
        return image_url
    
    @classmethod
    def filter_by_location(cls,location):
        image_url = Image.objects.filter(id = location)
        return image_url
    
    @classmethod
    def search_by_category(cls,search_term):
        images_url = cls.objects.filter(image_name__icontains=search_term)
        return images_url

    





class Picture(models.Model):
    picture_name = models.CharField(max_length=30)
    picture_description = models.TextField(max_length=100)
    picture_image = models.ImageField(upload_to='studio/')
    datep_posted = models.DateTimeField(default=timezone.now)
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)

   
    

    def __str__(self):
        return self.picture_name

  
