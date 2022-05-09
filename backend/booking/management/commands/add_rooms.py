from django.core.management.base import BaseCommand
from booking.models import Room
from .cities import records, city_names
import random


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Create Rooms '

    @staticmethod
    def _populate_data():
        all_us_cities = list(records.keys())
        all_rooms = ["Studio", "Suite", "Deluxe"]
        room_prices = [200, 300, 400, 500, 600]

        amenities = ["Daily Continental Breakfast",
                     "Access to fitness room",
                     "Access to Swimming Pool and Jacuzzi",
                     "Daily Parking",
                     "All meals included"]

        room_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        days_advance = [2, 3, 4, 5, 6]

        for room_name in range(101, 111):
            city = random.choice(city_names)
            selected_room_type = random.choice(all_rooms)
            selected_room_price = random.choice(room_prices)

            room_image_url = "https://raw.githubusercontent.com/aryan-jadon/SW-Engineering-Project-Images/main/R" + str(
                random.choice(room_range)) + '.jpg'

            print(room_image_url)

            Room.objects.get_or_create(room_no=str(room_name),
                                       room_type=selected_room_type,
                                       room_amenities=amenities,
                                       is_available=True,
                                       price=selected_room_price,
                                       no_of_days_advance=random.choice(days_advance),
                                       room_location=city,
                                       room_image=room_image_url
                                       )

    def handle(self, *args, **options):
        self._populate_data()
