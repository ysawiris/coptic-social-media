from django.test import TestCase, Client


# Create your tests here.

class PostList_Test(TestCase):
    """Tests that the pagesworks."""
    def test_api_route(self):
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/api/')
    
        self.assertEqual(response.status_code, 200)

    
