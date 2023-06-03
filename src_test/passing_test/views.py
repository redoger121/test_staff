from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django import forms

from tests.models import TestQuestions, Answers, Tests
from passing_test.models import *
from user_office.models import Office
from passing_test.forms import AnswerPassForm, AnswerFormSet


@login_required
def start_test(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    pas_test = PassedTests.objects.filter(name=test.name, user=request.user)
    if not pas_test:
        pas_test = PassedTests(user=request.user, name=test.name, theme_id=test.theme_id, test_id=pk,
                               main_test_id=test.pk)
        pas_test.save()
        questions = TestQuestions.objects.filter(for_test=pk)
        for item in questions:
            pas_question = PassedTestQuestions(name=item.name, for_test=pas_test)
            pas_question.save()
            answers = Answers.objects.filter(for_question=item.pk)

            for answ in answers:
                pas_answers = PassedAnswers(name=answ.name, real_answer=answ.answer_is_true,
                                            for_question=pas_question)
                pas_answers.save()

    pas_test = PassedTests.objects.get(name=test.name, user=request.user)
    context = {
        'test': pas_test,
    }

    pas_questions = PassedTestQuestions.objects.filter(for_test=pas_test.pk)
    context['questions'] = pas_questions

    answ = []
    for item in pas_questions:
        answ.append(item.pk)

    pas_answers = PassedAnswers.objects.filter(for_question__in=answ)
    context.update({'answers': pas_answers})

    if request.method == 'POST':
        ans_formset = AnswerFormSet(request.POST, queryset=pas_answers)
        i = 0
        for item in pas_questions:

            for form in ans_formset:

                if int(form['for_question'].data) == int(item.pk) and form['answer_is_true'].data == True:
                    i += 1
            print(i)
            if i == 0:

                print('не выбран ответ')
                return HttpResponseRedirect(reverse('test_passing:start_test', args=[pk]))

            else:
                i = 0
        if ans_formset.is_valid():
            ans_formset.save()

            pas_answers = PassedAnswers.objects.filter(for_question__in=answ)
            score = 0
            col_of_question = 0

            for question in pas_questions:
                col_of_question += 1
                numer_of_answers = 0
                number_of_correct_answers = 0

                for item in pas_answers:

                    if item.for_question == question:
                        numer_of_answers = numer_of_answers + 1
                        if item.real_answer == item.answer_is_true:
                            number_of_correct_answers += 1

                if number_of_correct_answers == numer_of_answers and numer_of_answers > 0:
                    score += 1
                    numer_of_answers = 0
                    number_of_correct_answers = 0

            real_score = 100 / col_of_question * score
            pas_test.score = real_score
            pas_test.test_closed = True
            pas_test.save()
            office = Office.objects.get(user_id=request.user, tests_id=pas_test.test_id)
            office.state_of_test = True
            office.save()
            test.visited += 1
            test.save()
            return HttpResponseRedirect(reverse('office:office'))
        else:
            print('Форма не валидна')

    else:
        ans_formset = AnswerFormSet(queryset=pas_answers)

    context['formset'] = ans_formset

    return render(request, 'passing_test/start_test.html', context)


@login_required
def list_of_passed_tests(request):
    passed_tests = PassedTests.objects.filter(user_id=request.user, test_closed=True)
    rait_list = []
    user = request.user
    for test in passed_tests:
        if Raiting.objects.filter(test=test.main_test, user=user):
            raiting = Raiting.objects.get(test=test.main_test, user=user)

            rait_dict = {'rait_test': raiting.test.pk, 'rait': raiting.mark}
            rait_list.append(rait_dict)

    context = {
        'rait_list': rait_list,
        'passed_tests': passed_tests,
    }
    print(rait_list)

    return render(request, 'passing_test/list_of_passed_tests.html', context)


def passed_test_detail(request, pk):
    test = get_object_or_404(PassedTests, pk=pk)
    questions = PassedTestQuestions.objects.filter(for_test=pk)

    answ = []
    for question in questions:
        answ.append(question.pk)

    answers = PassedAnswers.objects.filter(for_question__in=answ)

    context = {
        'test': test,
        'questions': questions,
        'answers': answers,

    }
    return render(request, 'passing_test/passed_test_detail.html', context)


from tests.models import Raiting


def raiting(request, pk, pk2):
    rait_test = PassedTests.objects.get(pk=pk)
    test=Tests.objects.get(id=rait_test.main_test.pk)
    mark = pk2
    user = request.user
    if not Raiting.objects.filter(test=test, user=user):
        rait = Raiting(test=test, user=user, mark=mark)
        rait.save()
        pas_test = PassedTests.objects.get(user_id=user.pk, main_test_id=test.pk)

        pas_test.rait = True
        pas_test.save()

        tests_raiting = Raiting.objects.filter(test=test)
        lenght = len(tests_raiting)
        sum = 0
        for test_raiting in tests_raiting:
            sum += test_raiting.mark

        test.test_rait = sum / lenght
        print(test.test_rait)
        test.save()
        print(test)
        print(lenght)
        return HttpResponseRedirect(reverse('test_passing:list_of_passed_tests'))
    else:
        return HttpResponseRedirect(reverse('test_passing:list_of_passed_tests'))
