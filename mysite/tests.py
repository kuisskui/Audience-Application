from django.test import TestCase
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.tests import OAuth2TestsMixin
from django.contrib.auth.models import User
from django.urls import reverse

callback_url = 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?client_id=1020628582950-uqlvo1ok0sfv8bbe92p6hm06ha687g8a.apps.googleusercontent.com&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&scope=profile%20email&response_type=code&state=wo2YqVWsepVX&access_type=online&service=lso&o2v=1&theme=glif&flowName=GeneralOAuthFlow'

class AllAuthTests(TestCase, OAuth2TestsMixin):
    def setUp(self):
        # Create a Site
        self.site = Site.objects.create(name="http://127.0.0.1:8000", domain="http://127.0.0.1:8000")
        
        # # Create a SocialApp for testing
        self.app = SocialApp.objects.create(
            provider="google",
            name="Google",
            client_id="1020628582950-uqlvo1ok0sfv8bbe92p6hm06ha687g8a.apps.googleusercontent.com",
            secret="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",
        )
        self.app.sites.add(self.site)
        self.app.callback_url = self.client.get(callback_url)

    def test_authentication_error(self):
        # Implement this test if needed
        pass

    def test_login(self):
        # Implement this test if needed
        pass

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AccountViewTests(TestCase):
    def setUp(self):
        self.user_data1 = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }
        self.user_data2 = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
            'gender': 'male',
            'age': '20',
            'country': 'Japan'
        }
        self.user = User.objects.create_user(**self.user_data1)
        self.register_url = reverse('register')  # Updated URL
        self.login_url = reverse('custom_login')  # Updated URL
        self.update_profile_url = reverse('update_profile')  # Updated URL
        self.logout_url = reverse('custom_logout')  # Updated URL

    # def test_register_view(self):
    #     response = self.client.post(self.register_url, data=self.user_data2, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Registration successful.")

    def test_register_view_invalid_data(self):
        invalid_data = {
            'username': '',  # Invalid data
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com',
        }
        response = self.client.post(self.register_url, data=invalid_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Unsuccessful registration. Invalid information.")

    # def test_custom_login_view(self):
    #     response = self.client.post(self.login_url, data=self.user_data, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertRedirects(response, reverse('audience:dashboard'))

    def test_custom_login_view_invalid_data(self):
        invalid_data = {
            'username': 'testuser',
            'password': 'invalidpassword',  # Invalid password
        }
        response = self.client.post(self.login_url, data=invalid_data, follow=True)
        self.assertEqual(response.status_code, 200)

    # def test_custom_logout_view(self):
    #     self.client.login(username='testuser', password='testpassword')
    #     response = self.client.post(reverse('account:logout'), follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertRedirects(response, reverse('audience:dashboard'))

    # def test_update_profile_view(self):
    #     self.client.login(username='testuser', password='testpassword')
    #     profile_data = {
    #         'gender': 'Male',
    #         'age': 30,
    #         'country': 'USA',
    #     }
    #     response = self.client.post(self.update_profile_url, data=profile_data, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Profile information updated successfully.")

    def test_update_profile_view_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')
        invalid_data = {
            'gender': '',  # Invalid data
            'age': 30,
            'country': 'USA',
        }
        response = self.client.post(self.update_profile_url, data=invalid_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Unsuccessful profile update. Invalid information.")

        invalid_data = {
            'gender': 'Male',
            'age': 30,
            'country': 'Invalid Country',  # Invalid country
        }
        response = self.client.post(self.update_profile_url, data=invalid_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Unsuccessful profile update. Invalid information.")

        # You can add more test cases to cover other scenarios as needed.
