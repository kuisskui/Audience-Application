from django.test import TestCase
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.socialaccount import views as socialaccount_views
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

