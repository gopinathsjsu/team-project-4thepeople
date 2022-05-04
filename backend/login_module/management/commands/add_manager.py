from django.core.management.base import BaseCommand
from login_module.models import RoomManager
from django.contrib.auth.hashers import make_password, check_password


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Create Manager '

    def _populate_data(self):
        password_hash = make_password("roommanager")
        RoomManager.objects.get_or_create(username="roommanager",
                                          password=password_hash,
                                          email="manager@gmail.com",
                                          contact="669234567"
                                          )

    def handle(self, *args, **options):
        self._populate_data()
