from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.nairobi = Location(photo_location='Nairobi')
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.nairobi.id)
        location.update_location('Kitengela')
        location = Location.get_location_id(self.nairobi.id)
        self.assertTrue(location.photo_location == 'Kitengela')
    
    def tearDown(self):
        self.nairobi.delete_location()
    
class CategoryTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.sports = Category(photo_category='Sports')
        self.sports.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.sports,Category))
    
    def tearDown(self):
        self.sports.delete_category()
    
    def test_updating_category(self):
        category = Category.get_category_id(self.sports.id)
        category.update_category('SUV')
        category = Category.get_category_id(self.sports.id)
        self.assertTrue(category.photo_category == 'SUV')
    
class ImageTestCase(TestCase):
    # Set Up Method
    def setUp(self):
        self.sports = Category(photo_category='Sports')
        self.sports.save_category()

        self.nairobi = Location(photo_location='Nairobi')
        self.nairobi.save_location()

        self.image = Image(name='Lamborghini', description='very first car', location=self.nairobi, category=self.sports)
        self.image.save_image()
    
    def tearDown(self):
        self.image.delete_image()
        self.sports.delete_category()
        self.nairobi.delete_location()
    
    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)
    
    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.image.id)
        self.assertTrue(images == self.image)

    def test_search_image(self):
        images = Image.search_image('Sports')
        self.assertTrue(len(images)>0)
    
    def test_filter_by_location(self):
        images = Image.filter_by_location('Nairobi')
        self.assertTrue(len(images)>0)
