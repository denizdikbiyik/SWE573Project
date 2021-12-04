from datetime import datetime
from django.test import TestCase

from social.models import Service

class ServiceModelTest(TestCase):              
    @classmethod

    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.up1 = UserProfile.objects.create(user=self.u1)

    def setUpTestData(self):                                     
        self.service = Service.objects.create(
            creater=self.u1,
            createddate=datetime.now,
            name="ServiceTest",
            picture='uploads/service_pictures/default.png',
            description="ServiceTestDescription",   
            servicedate=datetime.now,
            capacity=1,
            duration=1,
            is_given=False,
            is_taken=False
        ) 

    def test_it_has_information_fields(self):                   
        self.assertIsInstance(self.service.description, str)

    def test_it_has_timestamps(self):                           
        self.assertIsInstance(self.service.servicedate, datetime)