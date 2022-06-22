from django.test import TestCase
from .models import *

# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Kilimani = Location.objects.create(name="Kilimani")
        self.test_neighbourhood = Neighbourhood.objects.create(name='Kilimani',location='Nairobi',admin='Wambui',image='example.jpg',description='Beautiful place',occupants='1')
        self.test_neighbourhood.save()


    def test_save_method(self):
        self.test_neighbourhood.save()
        test_neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(test_neighbourhoods) > 0)
            
    
    def test_delete_method(self):
        self.Neighbourhood.delete_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)==0)   
        
    def tearDown(self):
        Neighbourhood.objects.all().delete()
        
        
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Prof= Profile( id = '1',bio='Happy', profile_picture = 'example.jpg',email='james@gmail.com',phone_number='0724580020',neighbourhood='Kilimani' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Prof,Profile)) 
        
        
class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Pos= Post( id = '1', user ='James',title='Happy', info = 'Happy day',neighbourhood='Kilimani')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pos,Post))        
                         
class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Comm= Post( id = '1', comment ='Nice',post='Happy', user = 'Wambui')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Comm,Comment)) 
        

class AuthorityTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Auth= Post( id = '1', name ='Police',email='police@gmail.com', contact = '707594873',neighbourhood='Kilimani' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Auth,Authority))
        

class HealthTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Heal= Heal( id = '1', name ='Hospital',email='hospital@gmail.com', contact = '707594873',neighbourhood='Kiliamani' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Heal,Health))   
        
        
class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Busi = Location.objects.create(name="Busi")

        self.test_business = Business.objects.create(name='Barber',image='example.jpg',user='Wambui',email='example@gmail.com',phone_number='072565676',neighbourhood='Kilimani')

        self.test_business.save()

    def test_save_method(self):
        self.test_business.save()
        test_business = Business.objects.all()
        self.assertTrue(len(test_business) > 0)
            
    
    def test_delete_method(self):
        self.Business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business)==0)   
        
    def tearDown(self):
        Business.objects.all().delete()  