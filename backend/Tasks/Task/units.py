# tasks/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import *

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(title='Test Task', description='Test Description', due_date='2023-12-31', status='Pending', owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Write similar tests for other CRUD operations

    # ...

