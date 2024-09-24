from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class UserAuthTests(TestCase):
    """
    Tests for user authentication, including login and logout functionalities.
    """
    def setUp(self):
        """
        Test to create a user with a username and password
        """
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login(self):
        """
        Test that a user can log in successfully
        """
        response = self.client.post(reverse('account_login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  # Expect a redirect on successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        """
        Test that a logged-in user can log out successfully
        """
        # Log the user in first
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)
