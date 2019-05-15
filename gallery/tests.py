from django.test import TestCase
from .models import Photographer, Image, Location, Category
from django.contrib.auth.models import User

# Create your tests here.
class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james = Photographer(first_name='James', last_name='Muriuki', email='james@moringaschool.com')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Photographer))
        

    def test_save_method(self):
        self.james.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)
    def test_display_method(self):
      self.james.display_photographer()
  
    def test_delete_method(self):
        self.james.delete_photographer()

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kenya = Location(location = 'nairobi')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya, Location))
        

    def test_save_method(self):
        self.kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    def test_display_method(self):
      self.kenya.display_location()
  
    def test_delete_method(self):
        self.kenya.delete_location()

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nature = Category(category = 'forest')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature, Category))
        

    def test_save_method(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    def test_display_method(self):
      self.nature.display_category()
  
    def test_delete_method(self):
        self.nature.delete_category()

class ImageTestClass(TestCase):
    # Set up method
    

    def setUp(self):
    
        self.photog = Photographer(email='nike')
        self.photog.save_photographer()
        self.locate = Location(location='nairobi')
        self.locate.save_location()
        self.categ = Category(category='forest')
        self.categ.save_category()

        self.image = Image(image_name='Picture1', image_description='tested image', photographer=self.photog, location=self.locate, category=self.categ)
        self.image.save_image()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
       
