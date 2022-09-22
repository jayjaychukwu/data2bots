from accounts.permissions import IsOwner
from rest_framework import generics
from rest_framework.response import Response

from .models import Order, Product
from .serializers import OrderSerializer


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(client=user)
