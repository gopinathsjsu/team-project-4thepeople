from django.urls import path
from .views import SearchRoom, BookRoom

urlpatterns = [
   path('search/', SearchRoom.as_view(), name="search-api-view"),
   path('booking/', BookRoom.as_view(), name="book-api-view"),
]