from django.core.management.base import BaseCommand
from customers.models import Customer
from faker import Faker


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Populate Data'

    def _populate_data(self):
        for entry in range(5001):
            print("Populating Entry {entry}".format(entry=entry))
            fake_gen = Faker()
            user_profile = fake_gen.profile()

            fake_username = user_profile['username']
            fake_password = user_profile['name']
            fake_email_address = user_profile['mail']
            fake_contact_number = fake_gen.phone_number()
            fake_address = fake_gen.street_address()
            fake_state = fake_gen.country_code()
            fake_zip_code = fake_gen.postcode()

            Customer.objects.get_or_create(username=fake_username,
                                password=fake_password,
                                email_address=fake_email_address,
                                contact_number=fake_contact_number,
                                address=fake_address,
                                state=fake_state,
                                zip_code=fake_zip_code
                                )

            # customer.save()

    def handle(self, *args, **options):
        self._populate_data()
