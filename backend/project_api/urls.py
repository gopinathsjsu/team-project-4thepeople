from django.urls import path
from .views import CustomersAPI,RoomDetails, ContactViews

urlpatterns = [
   path('customers/', CustomersAPI.as_view(), name="customer-api-view"),
   path('roomdetails/<str:datestring>', RoomDetails.as_view(), name="room-api-view"),
   path('contacts/', ContactViews.as_view(), name="contact-api-view"),
]
