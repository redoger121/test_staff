from django.core.management.base import BaseCommand
from authapp.models import TestingUser
from authapp.models import TestingUserProfile


class Command(BaseCommand):
    help = 'Update DB'

    def handle(self, *args, **options):
        users = TestingUser.objects.all()
        for user in users:
            users_profile = TestingUserProfile.objects.create(user=user)
            users_profile.save()
