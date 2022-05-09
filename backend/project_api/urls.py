from django.urls import path
from .views import SearchRoom, BookRoom, BookingDetails

urlpatterns = [
   path('search/', SearchRoom.as_view(), name="search-api-view"),
   path('booking/', BookRoom.as_view(), name="book-api-view"),
   path('booking_details/', BookingDetails.as_view(), name="booking-details-api-view"),
]