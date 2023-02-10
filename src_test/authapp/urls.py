from django.urls import path
from .views import *

urlpatterns=[
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('edit/', edit, name='edit'),
    path('change/password/', ChangePassword.as_view(), name='change_password'),
    path('user_bio/', user_bio, name='user_bio'),
]