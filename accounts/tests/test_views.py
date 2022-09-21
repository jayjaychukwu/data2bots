from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from .test_setup import TestSetUp


class ClientRegistrationTests(TestSetUp):
    # test that a user can register
    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.client_registration_info, format="json")
        self.assertEqual(res.data["user"]["username"], self.client_registration_info["username"]),
        self.assertEqual(res.data["user"]["email"], self.client_registration_info["email"])
        self.assertEqual(res.status_code, 200)

    # test that user can't register with no data
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)


class LoginTests(TestSetUp):
    # Test that user can login successfully
    def test_login_successful(self):
        self.client.post(self.register_url, self.client_registration_info, format="json")
        user = get_user_model().objects.get(email=self.client_registration_info["email"])
        data = {
            "username": self.client_registration_info["username"],
            "password": self.client_registration_info["password"],
        }
        res = self.client.post(self.login_url, data=data, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.data.keys()), ["expiry", "token"])


class EditUserDetailsTest(TestSetUp):

    # Tests if can edit their details
    def test_customer_can_change_their_details_successfully(self):
        self.client.post(self.register_url, self.client_registration_info, format="json")
        user = get_user_model().objects.get(email=self.client_registration_info["email"])
        data = {
            "username": self.client_registration_info["username"],
            "password": self.client_registration_info["password"],
        }
        res = self.client.post(self.login_url, data=data, format="json")
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Token " + res.data["token"])

        # testing that only one field can be changed successfully
        data = {"first_name": self.client_user_information["first_name"]}
        res = client.put(self.edit_url, data=data, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["first_name"], self.client_user_information["first_name"])

        # Testing that all the fields can be changed successfully
        data = {
            "first_name": self.client_user_information["first_name"],
            "last_name": self.client_user_information["last_name"],
            "gender": self.client_user_information["gender"],
            "phone_number": self.client_user_information["phone_number"],
            "address": self.client_user_information["address"],
        }
        resp = client.put(self.edit_url, data=data, format="json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["first_name"], self.client_user_information["first_name"])
        self.assertEqual(resp.data["last_name"], self.client_user_information["last_name"])
        self.assertEqual(resp.data["gender"], self.client_user_information["gender"])
        self.assertEqual(resp.data["phone_number"], str(self.client_user_information["phone_number"]))
        self.assertEqual(resp.data["address"], self.client_user_information["address"])
