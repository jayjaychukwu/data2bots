from accounts.models import CustomUser
from django.core.management import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        wr = open("accounts/users.txt", "w")

        for _ in range(5):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()

            CustomUser.objects.create(
                username=username,
                email=email,
                password=password,
            )

            wr.write(f"username: {username}, password:{password}\n")

        print("5 random users have been created")
