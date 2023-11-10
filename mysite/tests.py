import os
from pathlib import Path
from dotenv import load_dotenv
from django.test import TestCase
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.tests import OAuth2TestsMixin
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from .forms import NewUserForm
from django.urls import reverse

callback_url = os.getenv("GOOGLE_CALLBACK_URL")

class AllAuthTests(TestCase, OAuth2TestsMixin):
    def setUp(self):
        # Create a Site
        self.site = Site.objects.create(name="http://127.0.0.1:8000", domain="http://127.0.0.1:8000")
        
        # # Create a SocialApp for testing
        self.app = SocialApp.objects.create(
            provider="google",
            name="Google",
            client_id=os.getenv("GOOGLE_CLIENT_ID"),
            secret=os.getenv("GOOGLE_SECRET_KEY"),
        )
        self.app.sites.add(self.site)
        self.app.callback_url = self.client.get(callback_url)

    def test_authentication_error(self):
        # Implement this test if needed
        pass

    def test_login(self):
        # Implement this test if needed
        pass


class AccountViewTests(TestCase):
    def setUp(self):
        self.user_data1 = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }
        self.data2 = {
            'user': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
            'email': 'newuser@example.com',
            'gender': 'Male',
            'age': 25,
            'country': 'US',
        }
        self.user1 = User.objects.create_user(**self.user_data1)
        self.register_url = reverse('register')  # Updated URL
        self.login_url = reverse('custom_login')  # Updated URL
        self.update_profile_url = reverse('update_profile')  # Updated URL
        self.logout_url = reverse('custom_logout')  # Updated URL
