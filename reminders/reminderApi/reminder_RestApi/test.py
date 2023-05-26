from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Reminder_RestApi



class TestReminder_RestApi (TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_reminder_RestApi_list(self):
        url = '/reminder_RestApi/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Reminder_RestApi.objects.count())
    

    def test_get_reminder_RestApi_Reminder_RestApi(self):
        reminder_RestApi = Reminder_RestApi.objects.create(name="Badara Jammeh", age= 42)
        url = '/reminder_RestApi/{}/'.format(reminder_RestApi.id)
        response =  self.client.get(url)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Badara')
        self.assertEqual(response.data['age'], 42)
    
    def test_create_reminder_RestApi(self):
        url =  '/reminder_RestApi'
        data =  {'name': 'Badara Jammeh', 'age': 42}
        response = self.client.post(url, data, format= "json")
        self.assertEqual(response.status_code, status.HTTP_401_CREATED)
        
    
        self.assertEqual(response.data['name'], 'Badara Jammeh')
        self.assertEqual(response.data['age'], 42)
        self.assertTrue(Reminder_RestApi.objects.filter(name='Badara', age= 42).exists())

    def test_update_reminder_RestApi(self):
         reminder_RestApi = Reminder_RestApi.objects.create(name='John', age=42)
         url = '/reminder_RestApi/{}/'.format(reminder_RestApi.id)
         data = {'name': 'Badara Jammeh', 'age': 30}
         response = self.client.put(url, data, format='json')
 