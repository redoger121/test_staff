import codecs
import os, sys

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "src_test.settings"
import django

django.setup()

from sqlite3 import DatabaseError
import datetime as dt
from user_office.parsers import hh_ru
    # job_ru
from tests.models import ThemeOfTests
from user_office.models import Vacancy, Error, Url

ten_days_ago=dt.date.today()-dt.timedelta(10)
Vacancy.objects.filter(timestamp__lte=ten_days_ago).delete()

parsers = (
    (hh_ru, 'hh.ru'),
    # (job_ru, 'job.ru')

)

themes = ThemeOfTests.objects.all().values()

themes_list = set(q['id'] for q in themes)

qs = Url.objects.all().values()
url_dict = {q['theme_id']: q['url_data'] for q in qs}

urls = []

for item in themes_list:
    if item in url_dict:
        tmp = {}
        tmp['theme_id'] = item
        tmp['url_data'] = url_dict[item]
        urls.append(tmp)




jobs = []
errors = []

for data in urls:

    for func, key in parsers:
        url = data['url_data'][key]
        theme = ThemeOfTests.objects.get(pk=data['theme_id'])
        j, e = func(url, theme)
        jobs += j
        errors += e



for job in jobs:


    v=Vacancy.objects.filter(href=job['href'])

    if not v:
        v=Vacancy(**job)
        v.save()
    else:
        pass


if errors:
    er = Error(data=errors).save()


