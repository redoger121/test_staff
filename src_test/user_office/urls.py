from django.urls import path
from .views import *

urlpatterns=[
    path('', office, name='office'),
    path('add/<int:pk>/', add_test_to_office, name='add'),
    path('delete/<int:pk>/', remove_test_from_office, name='delete'),
    path('view/vacancies/', view_vacancy, name='view_vacancy'),
]