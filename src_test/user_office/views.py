from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Office, Vacancy
from tests.models import Tests
from passing_test.models import PassedTests

@login_required
def office(request):
    office_items = Office.objects.filter(user=request.user).order_by('tests__theme_id')

    context = {
        'office_items': office_items
    }
    return render(request, 'user_office/office.html', context)


@login_required
def add_test_to_office(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('tests:test_questions', args=[[pk]]))

    test = get_object_or_404(Tests, pk=pk)
    office = Office.objects.filter(user=request.user, tests=test).first()

    if not office:
        office = Office(user=request.user, tests=test)
        office.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def remove_test_from_office(request, pk):
    office_record=get_object_or_404(Office, pk=pk)
    office_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def view_vacancy(request):
    passed_tests= PassedTests.objects.filter(user=request.user)
    score=0
    vacancy_theme=[]
    for test in passed_tests:
        if test.score >score:
            score=test.score
            vacancy_theme.clear()
            vacancy_theme.append(test.theme_id)
        elif test.score ==score and score>0:
            vacancy_theme.append(test.theme_id)
    vacancies=Vacancy.objects.filter(theme_id__in=vacancy_theme).order_by('-timestamp')

    context={
        'vacancies':vacancies,
    }
    return render(request, 'user_office/view_vacancies.html', context)
