import jsonfield
from django.db import models
from django.conf import settings
from tests.models import Tests, ThemeOfTests

def default_urls():
    return {'hh.ru': "",  'job.ru':""}



class Office(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='office')
    tests = models.ForeignKey(Tests, on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    state_of_test = models.BooleanField(default=0)


class Vacancy(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    href = models.URLField(unique=True)
    company = models.CharField(max_length=250, verbose_name='Компания')
    content = models.TextField(verbose_name='Описание вакансии')
    pay = models.CharField(max_length=50)
    theme=models.ForeignKey(ThemeOfTests, on_delete=models.CASCADE, null=True)
    timestamp = models.DateField(auto_now_add=True)
    img_href=models.URLField(blank=True)

    def __str__(self):
        return self.title


class Error(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    data=jsonfield.JSONField()

class Url(models.Model):
    theme=models.ForeignKey(ThemeOfTests, on_delete=models.CASCADE, unique=True)
    url_data=jsonfield.JSONField(default=default_urls())


