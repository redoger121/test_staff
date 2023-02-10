from django.urls import path
from adminapp.views import *


urlpatterns=[

    path('admin/panel/', admin_panel, name='admin_panel'),
    path('users/read/', testing_users, name='users'),
    path('users/create/', user_create, name='user_create'),
    path('users/update/<int:pk>/', update_user, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),
    path('themes/', themes, name='themes'),
    # path('themes/create/', ThemeCreateView.as_view(), name='theme_create'),
    # path('themes/update/<int:pk>/', ThemeUpdateView.as_view(), name='theme_update'),
    # path('theme/delete/<int:pk>/', ThemeDeleteView.as_view(), name='theme_delete'),
    path('admin/panel/theme/<int:pk>/', theme_delete, name='theme_delete'),
    path('theme/tests/<int:pk>', tests_by_theme, name='tests_by_theme'),
    path('theme/test/questions/<int:pk>/', tests_questions, name='tests_questions'),
    path('theme/test/create/<int:pk>', test_create, name='test_create'),
    path('theme/test/add/questions/<int:pk>/', add_questions_to_test, name='add_questions_to_test'),
    path('theme/test/add/answer/<int:pk>', add_answers_to_question, name='add_answer_to_question'),
    path('theme/test/delete/<int:pk>', delete_test, name='delete_test'),
    path('theme/test/answer/delete/<int:pk>/', delete_answer, name='delete_answer'),
    path('theme/test/question/delete/<int:pk>/', delete_question, name='delete_question'),
    path('theme/test/change/name/<int:pk>/', edit_test_name, name='edit_test_name'),
    path('list/tests/moderate/', list_of_tests_to_moderate, name='moderate_list'),
    path('test/moderate/<int:pk>/', moderate_test, name='moderate_test'),
    path('test/approve/<int:pk>/', approve_test, name='approve_test'),
    path('test/decline/<int:pk>/', decline_test, name='decline_test'),
    path('parsers/urls/', show_parsers_url, name='show_parsers_url'),
    path('parsers/add/urls/<int:pk>', add_urls_to_parsers, name='add_urls_to_parsers'),
    path('parsers/delete/urls/<int:pk>/', delete_url, name='delete_url'),

]