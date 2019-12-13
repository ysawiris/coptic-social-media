import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from media.models import Post


class NewsFeedListView_Test(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/')
    
        self.assertEqual(response.status_code, 200)

class ProfileListView_Test(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/profile/')
    
        self.assertEqual(response.status_code, 200)

class PostCreateNewView_Test(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/create_new/')
    
        self.assertEqual(response.status_code, 200)
