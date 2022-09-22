from accounts.tests.test_setup import TestSetUp
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


class GetOrdersTest(TestSetUp):
    order_list_url = reverse("orders")

    def test_user_can_get_orders(self):
        self.client.post(self.register_url, self.client_registration_info, format="json")
        user = get_user_model().objects.get(email=self.client_registration_info["email"])
        data = {
            "username": self.client_registration_info["username"],
            "password": self.client_registration_info["password"],
        }
        res = self.client.post(self.login_url, data=data, format="json")
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Token " + res.data["token"])

        # Test that user can get orders
        res = client.get(self.order_list_url)
        self.assertEqual(res.status_code, 200)
