import random

from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.edit_url = reverse("update")
        self.fake = Faker()

        self.client_registration_info = {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.password(),
        }

        self.client_user_information = {
            "last_name": self.fake.last_name(),
            "first_name": self.fake.first_name(),
            "gender": random.choice(["MALE", "FEMALE"]),
            "phone_number": random.randint(10000000000, 99999999999),
            "address": self.fake.address(),
        }

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
