import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from media.models import Post


class NewsFeedListView_Test(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
        user = User.objects.create()
        self.client.force_login(user)
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/')
    
        self.assertEqual(response.status_code, 200)



class PostCreateNewView_Test(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
        user = User.objects.create()
        self.client.force_login(user)
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/create_new/')
    
        self.assertEqual(response.status_code, 200)
    
    def test_multiple_pages(self):
        #Create a user for ths test 
        user = User.objects.create()
        self.client.force_login(user)

        #Create and save Pages to the Database 
        Post.objects.create(content="test", author=user)
        Post.objects.create(content="test", author=user)

        #Make a GET request, and test route returns 200
        response = self.client.get('/create_new/')
    
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = Post.objects.all()
        self.assertEqual(len(responses), 2)

