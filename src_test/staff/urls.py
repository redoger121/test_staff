from django.urls import path

from .views import *


urlpatterns=[
    path('themes/', themes, name='themes'),
    path('tests/', tests, name='tests'),
    path('theme/test/questions/<int:pk>/', tests_questions, name='test_questions'),
    path('theme/test/create/', test_create, name='tests_create'),
    path('theme/test/add/questions/<int:pk>/', add_questions_to_test, name='add_questions_to_test'),
    path('theme/test/add/answer/<int:pk>', add_answers_to_question, name='add_answer_to_question'),
    path('theme/test/delete/<int:pk>', delete_test, name='delete_test'),
    path('theme/test/answer/delete/<int:pk>/', delete_answer, name='delete_answer'),
    path('theme/test/question/delete/<int:pk>/', delete_question, name='delete_question'),
    path('theme/test/change/name/<int:pk>/', edit_test_name, name='edit_test_name'),
    path('test/send/moderate/<int:pk>/', send_to_moderate, name='send_to_moderate'),

]