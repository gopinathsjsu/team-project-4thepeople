from django.urls import path
from .views import CustomersAPI

urlpatterns = [
   path('customers/', CustomersAPI.as_view(), name="customer-api-view"),
]
