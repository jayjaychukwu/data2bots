from django.urls import path

from orders.views import OrderListAPIView

urlpatterns = [
    path("", OrderListAPIView.as_view(), name="orders"),
]
