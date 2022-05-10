from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.


class RoomViewTestCase(TestCase):
    def test_add_room(self):
        room_record = {
            "room_no": "126",
            "room_type": "suite",
            "price": 300.0,
            "room_location": "sanjose",
            "room_image": "http://image",
            "no_of_days_advance": 2
        }
        response = self.client.post('/api/search/', room_record)
        self.assertEqual(response.status_code, 200)

    def test_add_duplicate_room(self):
        room_record1 = {
            "room_no": "122",
            "room_type": "suite",
            "price": 300.0,
            "room_location": "sanjose",
            "room_image": "http://image",
            "no_of_days_advance": 2
        }
        response1 = self.client.post('/api/search/', room_record1)
        room_record2 = {
            "room_no": "122",
            "room_type": "studio",
            "price": 300.0,
            "room_location": "sanjose",
            "room_image": "http://image",
            "no_of_days_advance": 2
        }
        response2 = self.client.post('/api/search/', room_record2)
        self.assertEqual(response2.status_code, 400)

    def test_get_roomSearch(self):
        room_record = {
            "room_no": "123",
            "room_type": "suite",
            "price": 300.0,
            "room_location": "sanjose",
            "room_image": "http://image",
            "no_of_days_advance": 2
        }
        response_post = self.client.post('/api/search/', room_record)
        response = self.client.get('/api/search/')
        self.assertEqual(response.status_code, 200)

class BookRommTestCase(TestCase):
    def test_bookRoom(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        # c.force_login(user)
        logged_in = c.login(username='testuser', password='12345')
        room_record2 = {
            "room_no": "131",
            "room_type": "studio",
            "price": 300.0,
            "room_location": "sanjose",
            "room_image": "http://image",
            "no_of_days_advance": 2
        }
        response2 = self.client.post('/api/search/', room_record2)
        booking_record = {
            "room_no": 131,
            "username": "testuser",
            "number_of_guests": "2",
            "booking_location": "sanjose",
            "booking_room_type": "studio",
            "start_day": '2022-05-16',
            "end_day": '2022-05-17',
            "room_price": 300.0,
            "booking_amenities": "All meals included,Daily Parking"
        }
        response_post = self.client.post('/api/booking/', booking_record)
        self.assertEqual(response_post.status_code, 200)
