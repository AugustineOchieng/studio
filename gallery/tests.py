from django.test import TestCase
from .models import Photographer, Image
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

class ImageTestClass(TestCase):
    # Set up method
    

    def setUp(self):
    
        self.photog = Photographer(first_name='nike')
        self.photog.save_photographer()

        self.Picture1 = Image(image_name = 'Picture1', image_description='tested image', image_url='url', Photographer=self.photog)
        
