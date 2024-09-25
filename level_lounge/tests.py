from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# AI and Reddit (r/django) leveraged to help
# configure tests and check errors


class UserAuthTests(TestCase):
    """
    Tests for user authentication, including login and logout functionalities.
    """

    def setUp(self):
        """
        Test to create a user with a username and password
        """
        self.user = User.objects.create_user(
            username='testuser', password='password123')

    def test_login(self):
        """
        Test that a user can log in successfully
        """
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        print(f"Login URL: {reverse('login')}")
        print(f"Response Status Code: {response.status_code}")
        # Expect a redirect on successful login
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        """
        Test that a logged-in user can log out successfully
        """
        # Log the user in first
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('logout'))
        print(f"Logout URL: {reverse('logout')}")
        print(f"Response Status Code: {response.status_code}")
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)
