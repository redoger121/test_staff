from django.urls import path
from .views import *

urlpatterns=[
    path('', main, name='main'),
    path('tests/', tests, name='tests'),
    path('themes/', themes, name='themes'),
    path('testsbytheme/<int:pk>/', tests_by_theme, name='tests_by_theme'),
    path('testquestion/<int:pk>/', tests_questions, name='test_questions'),
    path('actual/tests/', actual_tests, name='actual_tests'),
    path('new/tests/', new_tests, name='new_tests'),
    path('misjudged/tests/', misjudged_tests, name='misjudged_tests'),
    # path('create_test/', TestAddView.as_view(), name='create_test'),


]