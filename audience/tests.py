import os
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from user_profile.models import UserProfile
import time


class Person:
    def __init__(self, username, password, gender, age, country, sport_ids):
        self.username = username
        self.password = password
        self.gender = gender
        self.age = age
        self.country = country
        self.sport_ids = sport_ids


class SubscribeTestCase(TestCase):
    def setUp(self):
        self.person = Person("username", "password", "Male", "25", "USA", "1,2,3")
        self.client = Client()
        self.user = User.objects.create_user(username=self.person.username, password=self.person.password)
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            gender=self.person.gender,
            age=self.person.age,
            country=self.person.country,
            sport_ids=self.person.sport_ids
        )

    def login(self):
        self.client.login(username=self.person.username, password=self.person.password)

    def test_unauth_subscribe(self):
        response = self.client.post("/subscribe/1")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/subscribe/1")

    def test_auth_subscribe(self):
        self.login()  # Log in the user
        response = self.client.post("/subscribe/1")
        self.assertEqual(response.status_code, 302)

    def test_auth_unsubscribe(self):
        self.login()  # Log in the user
        response = self.client.post("/unsubscribe/1")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/profile/")
