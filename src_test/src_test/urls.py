
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', include(('adminapp.urls', 'admin'))),
    path('', include(('tests.urls', 'tests'))),
    path('auth/', include(('authapp.urls', 'auth'))),
    path('', include('social_django.urls', namespace='social')),
    path('office/', include(('user_office.urls', 'office'))),
    path('test/passing/', include(('passing_test.urls', 'test_passing'))),
    path('staff/', include(('staff.urls', 'staff'))),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )