from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class TestingUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)


class TestingUserProfile(models.Model):
    MALE = 'М'
    FEMALE = 'Ж'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(TestingUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    aboutMe = models.CharField(verbose_name='О себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=TestingUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            TestingUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=TestingUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.testinguserprofile.save()
