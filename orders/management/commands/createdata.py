import random
from distutils.command.clean import clean

import faker.providers
from accounts.models import CustomUser
from django.core.management.base import BaseCommand
from faker import Faker
from orders.models import Order, Product

CATEGORIES = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]

PRODUCTS = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]

PAYMENT = [
    "Card",
    "Transfer",
    "Cash",
]
STATUS = ["Placed" "Progress", "Shipped", "Out", "Delivered"]
DELIVERY = ["Pickup", "House"]


class Provider(faker.providers.BaseProvider):
    def product(self):
        return self.random_element(PRODUCTS)

    def category(self):
        return self.random_element(CATEGORIES)


class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)

        for _ in range(30):
            name = fake.product() + fake.name()[:4]
            description = fake.text(max_nb_chars=40)
            price = round(random.uniform(100.0, 9999.99), 2)
            vendor = fake.category() or fake.name()

            Product.objects.create(
                name=name,
                description=description,
                price=price,
                vendor=vendor,
            )

        print("30 products generated")

        for _ in range(15):

            product_selection = random.randint(1, int(Product.objects.all().count()))

            user_list = list(CustomUser.objects.all().values_list("username", flat=True))
            user_selection = random.choices(user_list)

            number = random.randint(1000, 99999999)
            total_price = Product.objects.get(id=product_selection).price
            product = Product.objects.get(id=product_selection)
            client = CustomUser.objects.get(username=user_selection[0])
            status = random.choices(STATUS)
            payment_method = random.choices(PAYMENT)
            delivery_option = random.choices(DELIVERY)

            Order.objects.create(
                number=number,
                total_price=total_price,
                product=product,
                client=client,
                status=status,
                payment_method=payment_method,
                delivery_option=delivery_option,
            )

        print("15 orders generated")
