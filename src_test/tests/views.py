from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView

from .models import *
from .forms import *
from django.shortcuts import HttpResponseRedirect
from authapp.models import TestingUser
from user_office.models import Vacancy
from tests.models import Tests, ThemeOfTests


# Create your views here.

def main(request):
    simple_users = len(TestingUser.objects.all())
    staff_users = len(TestingUser.objects.filter(is_staff=True))
    vacancies = len(Vacancy.objects.all())
    tests = len(Tests.objects.all())


    new_tests=Tests.objects.order_by('-date')[:6]
    actual_tests=Tests.objects.order_by('-test_rait')[:6]


    context = {
        'simple_users': simple_users,
        'staff_users': staff_users,
        'vacancies': vacancies,
        'tests': tests,
        'new_tests': new_tests,
        'actual_tests':actual_tests,

    }

    return render(request, 'tests/index2.html', context)


def tests(request):
    themes = ThemeOfTests.objects.all()
    tests = Tests.objects.filter(moderate='MO')

    if request.method == 'POST':
        form =FindTest(request.POST)


        if form.is_valid():
            tests=Tests.objects.filter(name__contains=form['name'].data, moderate='MO')

            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
            }
            return render(request, 'tests/tests.html', context)
        else:
            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            form = FindTest()
            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
            }
            return render(request, 'tests/tests.html', context)


    else:

        paginator = Paginator(tests, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = FindTest()
        context = {
            'form': form,
            'tests': page_obj,
            'themes': themes,
        }

        return render(request, 'tests/tests.html', context)



def actual_tests(request):
    themes = ThemeOfTests.objects.all()
    tests = Tests.objects.filter(moderate='MO').order_by('-test_rait')

    if request.method == 'POST':
        form =FindTest(request.POST)


        if form.is_valid():
            tests=Tests.objects.filter(name__contains=form['name'].data, moderate='MO')

            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
            }
            return render(request, 'tests/tests.html', context)
        else:
            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            form = FindTest()
            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
            }
            return render(request, 'tests/tests.html', context)


    else:

        paginator = Paginator(tests, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = FindTest()
        context = {
            'form': form,
            'tests': page_obj,
            'themes': themes,
        }

        return render(request, 'tests/tests.html', context)



def new_tests(request):
    themes = ThemeOfTests.objects.all()
    tests = Tests.objects.filter(moderate='MO').order_by('-date')

    if request.method == 'POST':
        form =FindTest(request.POST)


        if form.is_valid():
            tests=Tests.objects.filter(name__contains=form['name'].data, moderate='MO')

            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
            }
            return render(request, 'tests/tests.html', context)
        else:
            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            form = FindTest()
            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
            }
            return render(request, 'tests/tests.html', context)


    else:

        paginator = Paginator(tests, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = FindTest()
        context = {
            'form': form,
            'tests': page_obj,
            'themes': themes,
        }

        return render(request, 'tests/tests.html', context)


def misjudged_tests(request):
    themes = ThemeOfTests.objects.all()
    tests = Tests.objects.filter(moderate='MO').order_by('test_rait')

    if request.method == 'POST':
        form =FindTest(request.POST)


        if form.is_valid():
            tests=Tests.objects.filter(name__contains=form['name'].data, moderate='MO')

            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
            }
            return render(request, 'tests/tests.html', context)
        else:
            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            form = FindTest()
            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
            }
            return render(request, 'tests/tests.html', context)


    else:

        paginator = Paginator(tests, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = FindTest()
        context = {
            'form': form,
            'tests': page_obj,
            'themes': themes,
        }

        return render(request, 'tests/tests.html', context)




def themes(request):
    themes_list = ThemeOfTests.objects.all()

    context = {
        'themes_list': themes_list
    }
    return render(request, 'tests/themes_list.html', context)


def tests_by_theme(request, pk):
    theme = get_object_or_404(ThemeOfTests, pk=pk)
    tests = Tests.objects.filter(theme_id=pk, moderate='MO')
    themes = ThemeOfTests.objects.all()

    if request.method == 'POST':
        form = FindTest(request.POST)

        if form.is_valid():
            tests = Tests.objects.filter(name__contains=form['name'].data,  moderate='MO', theme_id=theme)
            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)


            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
                'tests_theme': theme,
            }
            return render(request, 'tests/tests.html', context)
        else:
            paginator = Paginator(tests, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'form': form,
                'tests': page_obj,
                'themes': themes,
                'tests_theme': theme,
            }
            return render(request, 'tests/tests.html', context)


    else:

        paginator = Paginator(tests, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        form = FindTest()

        context = {
            'form': form,
            'tests': page_obj,
            'themes': themes,
            'tests_theme': theme,
        }
        return render(request, 'tests/tests.html', context)


def tests_questions(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    context = {
        'test': test,
    }
    questions = TestQuestions.objects.filter(for_test=pk)
    if questions:
        context['questions'] = questions
    else:
        HttpResponseRedirect(reverse('tests:main'))

    answ = []
    for item in questions:
        answ.append(item.pk)

    answers = Answers.objects.filter(for_question__in=answ)
    if answers:
        context.update({'answers': answers})
    return render(request, 'tests/test_detail.html', context)
