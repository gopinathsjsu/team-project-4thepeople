import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_management.settings')
django.setup()

from .models import Customer

fake_gen = Faker()


def populate_entries(N=30):
    for entry in range(N):
        user_profile = fake_gen.profile()

        fake_username = user_profile['username']
        fake_password = user_profile['name']
        fake_email_address = user_profile['mail']
        fake_contact_number = fake_gen.phone_number()
        fake_address = fake_gen.street_address()
        fake_state = fake_gen.country_code()
        fake_zip_code = fake_gen.postcode()

        customer_entry = Customer.objects.get_or_create(username=fake_username,
                                                        password=fake_password,
                                                        email_address=fake_email_address,
                                                        contact_number = fake_contact_number,
                                                        address = fake_address,
                                                        state = fake_state,
                                                        zip_code = fake_zip_code
                                                        )


if __name__ == '__main__':
    print('Populating data...')
    populate_entries(30)
    print('Populating complete')
