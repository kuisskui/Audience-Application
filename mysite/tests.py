import os
from django.test import TestCase
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.tests import OAuth2TestsMixin
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from django.urls import reverse

callback_url = os.getenv("GOOGLE_CALLBACK_URL")

# class AllAuthTests(TestCase, OAuth2TestsMixin):
#     def setUp(self):
#         # Create a Site
#         self.site = Site.objects.create(name="http://127.0.0.1:8000", domain="http://127.0.0.1:8000")
        
#         # # Create a SocialApp for testing
#         self.app = SocialApp.objects.create(
#             provider="google",
#             name="Google",
#             client_id=os.getenv("GOOGLE_CLIENT_ID"),
#             secret=os.getenv("GOOGLE_SECRET_KEY"),
#         )
#         self.app.sites.add(self.site)
#         self.app.callback_url = self.client.get(callback_url)

#     def test_authentication_error(self):
#         # Implement this test if needed
#         pass

#     def test_login(self):
#         # Implement this test if needed
#         pass


class AccountViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            gender='Male',
            age='25',
            country='USA',
            sport_ids='1,2,3'
        )
        self.register_url = reverse('register')
        self.login_url = reverse('custom_login')
        self.update_profile_url = reverse('update_profile')
        self.logout_url = reverse('custom_logout')

    def test_user_profile_creation(self):
        self.assertIsInstance(self.user_profile, UserProfile)
        self.assertEqual(str(self.user_profile), f'{self.user.username} Profile')
        
    def test_user_profile_fields(self):
        # Test the individual fields of the UserProfile model
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.gender, 'Male')
        self.assertEqual(self.user_profile.age, '25')
        self.assertEqual(self.user_profile.country, 'USA')
        self.assertEqual(self.user_profile.sport_ids, '1,2,3')
        
