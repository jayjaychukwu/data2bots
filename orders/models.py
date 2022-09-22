from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Order(models.Model):
    PAY_WITH_CARD = "CARD"
    PAY_WITH_BANK_TRANSFER = "TRANSFER"
    PAY_CASH_ON_DELIVERY = "CASH"
    PAYMENT_METHOD = (
        (PAY_WITH_CARD, "Card"),
        (PAY_WITH_BANK_TRANSFER, "Transfer"),
        (PAY_CASH_ON_DELIVERY, "Cash"),
    )

    STATUS_1 = "ORDER_PLACED"
    STATUS_2 = "ORDER_IN_PROGRESS"
    STATUS_3 = "SHIPPED"
    STATUS_4 = "OUT_FOR_DELIVERY"
    STATUS_5 = "DELIVERED"
    STATUSES = (
        (STATUS_1, "Placed"),
        (STATUS_2, "Progress"),
        (STATUS_3, "Shipped"),
        (STATUS_4, "Out"),
        (STATUS_5, "Delivered"),
    )

    DELIVERY_PICKUP_STATION = "PICKUP"
    DELIVERY_HOUSE_DELIVERY = "HOUSE_DELIVERY"
    DELIVERIES = (
        (DELIVERY_PICKUP_STATION, "Pickup"),
        (DELIVERY_HOUSE_DELIVERY, "House"),
    )

    number = models.IntegerField(unique=True)
    placed_on = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT, related_name="order")
    client = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(max_length=20, choices=STATUSES)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    delivery_option = models.CharField(max_length=20, choices=DELIVERIES)

    def __str__(self):
        return str(self.number)
