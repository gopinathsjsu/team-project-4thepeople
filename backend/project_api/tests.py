from django.test import TestCase

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
