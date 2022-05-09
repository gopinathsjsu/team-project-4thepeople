from django.test import TestCase

# Create your tests here.

class BookingViewTestCase(TestCase):
    def test_get_bookedRooms(self):
        data = {
            "username":"testuser"
        }
        response  = self.client.get('/api/booking/', data)
        self.assertEqual(response.status_code, 200)

class SearchRoomView(TestCase):
    def test_get_bookedRoomscase1(self):
        data = {
            "location":"testlocation"
        }
        response  = self.client.get('/api/booking/', data)
        self.assertEqual(response.status_code, 200)

    def test_get_bookedRoomsCase2(self):
        data = {
            "username":"testuser"
        }
        response  = self.client.get('/api/booking/', data)
        self.assertEqual(response.status_code, 200)

    def test_get_bookedRoomsCase3(self):
        data = {
            "price_start":"200",
            "price_end" : "400"
        }
        response  = self.client.get('/api/booking/', data)
        self.assertEqual(response.status_code, 200)

    def test_get_bookedRoomsCase4(self):
        data = {
            "username":"testuser",
            "price_start":"200",
            "price_end" : "400",
            "price_start":"200",
            "price_end" : "400"
        }
        response  = self.client.get('/api/booking/', data)
        self.assertEqual(response.status_code, 200)
