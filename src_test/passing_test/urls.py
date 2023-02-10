from django.urls import path
from .views import *


urlpatterns=[
    path('<int:pk>', start_test, name='start_test'),
    path('list/passed/tests', list_of_passed_tests, name='list_of_passed_tests'),
    path('passed/test/detail/<int:pk>/', passed_test_detail, name='passed_test_detail'),
    path('list/passed/tests/<int:pk>/<int:pk2>', raiting, name='raiting'),
]