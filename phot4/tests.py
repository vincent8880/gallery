from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.india = Location(photo_location='India')
        self.india.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.india,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.india.id)
        location.update_location('paris')
        location = Location.get_location_id(self.india.id)
        self.assertTrue(location.photo_location == 'paris')
    
    def tearDown(self):
        self.india.delete_location()
    
class CategoryTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.food = Category(photo_category='food')
        self.food.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))
    
    def tearDown(self):
        self.food.delete_category()
    
    def test_updating_category(self):
        category = Category.get_category_id(self.food.id)
        category.update_category('ugali')
        category = Category.get_category_id(self.food.id)
        self.assertTrue(category.photo_category == 'ugali')
    
