from django.urls import path
from .views import SendMailView

urlpatterns = [
    path('sendmail/', SendMailView.as_view(), name="send_mail-api-view"),
]
