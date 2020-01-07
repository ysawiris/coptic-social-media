from django.test import TestCase

# Create your tests here.
class SignUpView_Test(TestCase):
    """Tests that the pagesworks."""
    def test_signup_route(self):
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/accounts/signup/')
    
        self.assertEqual(response.status_code, 200)

    
    def test_login_route(self):
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/accounts/login/')
    
        self.assertEqual(response.status_code, 200)

class ProfileListView_Test(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
        user = User.objects.create()
        self.client.force_login(user)
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/profile/')
    
        self.assertEqual(response.status_code, 200)