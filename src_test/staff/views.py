from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from tests.forms import TestForm, QuestionFormSet, QuestionsForm, QuestionFormSet_optional, TestName, \
    AnswersFormset_optional, AnswersFormset
from tests.models import ThemeOfTests, Tests, TestQuestions, Answers
from user_office.models import Office


def themes(request):
    themes_list = ThemeOfTests.objects.all()

    context = {
        'themes_list': themes_list
    }
    return render(request, 'staff/themes_list.html', context)


@login_required
def tests(request):

    tests = Tests.objects.filter(creator=request.user)

    context = {

        'tests': tests,
    }
    print(tests)
    return render(request, 'staff/tests_by_theme.html', context)



# РАботает
def test_create(request):
    # them = get_object_or_404(ThemeOfTests, pk=pk)
    context = {}
    if request.method == 'POST':

        test_form = TestForm(request.POST, request.FILES)
        test_name = test_form['name'].data
        # test_creator = test_form['creator'].data
        test_them = test_form['theme_id'].data
        test_image = test_form['image'].data
        print(test_form)
        test_object = Tests.objects.filter(name=test_name, creator=request.user, theme_id=test_them)
        if test_object.count() > 0:
            print('у вас уже есть такой тест')
            return HttpResponseRedirect(reverse('staff:test_create'))
        if test_form.is_valid():
            test_form.save()
            test_object = Tests.objects.get(name=test_name, creator=request.user, theme_id=test_them)
            context['name'] = test_object


    else:
        test_form = TestForm(initial={'creator': request.user})

    context['test_form'] = test_form
    return render(request, 'staff/test_create.html', context)

# РАботает
@login_required
def tests_questions(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    context = {
        'test': test,
    }

    if request.method == 'POST':
        form_question = QuestionFormSet_optional(request.POST)
        test_name_form = TestName(request.POST)
        answer_formset = AnswersFormset_optional(request.POST)

        if test_name_form.is_valid() and test_name_form['name'].data != test.name:
            print(test_name_form['name'].data)
            if not Tests.objects.filter(name=test_name_form['name'].data, pk=test.pk):
                test.name = test_name_form['name'].data
                test.save()

        for form in answer_formset:
            if form.is_valid():
                form.save()

        for form in form_question:
            if form.is_valid():
                question_pk = form['id'].data

                question = get_object_or_404(TestQuestions, pk=question_pk)
                question.name = form['name'].data
                question.save()




            else:
                print('что то пошло не так')

        return HttpResponseRedirect(reverse('staff:test_questions', args=[test.pk]))

    else:
        form_question = QuestionFormSet_optional(queryset=TestQuestions.objects.filter(for_test=test.pk))

        test_name_form = TestName(initial={'name': test.name})

        questions = TestQuestions.objects.filter(for_test=pk)

        answer_formset = AnswersFormset_optional(queryset=Answers.objects.filter(for_question__in=questions))

        context['answer_formset'] = answer_formset
        context['test_name_form'] = test_name_form
        context['questions'] = questions
        context['form_question'] = form_question
        answ = []

        for item in questions:
            answ.append(item.pk)

        answers = Answers.objects.filter(for_question__in=answ)

        context.update({'answers': answers})
    return render(request, 'staff/tests_detail.html', context)

# РАботает
def add_questions_to_test(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    # queryset = TestQuestions.objects.filter(for_test=pk)
    context = {
        'test': test,
    }

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST)
        if formset.is_valid():
            formset.save()

            questions = TestQuestions.objects.filter(for_test=test.pk)
            test.questionsNum = len(questions)
            test.save()
            context['test_formset'] = formset
            return HttpResponseRedirect(reverse('staff:test_questions', args=[test.pk]))


    else:
        formset = QuestionFormSet(queryset=TestQuestions.objects.none(), initial=[{'for_test': test.pk}])
        context['test_formset'] = formset
    return render(request, 'staff/test_update.html', context)

# РАботает
def add_answers_to_question(request, pk):
    question = get_object_or_404(TestQuestions, pk=pk)
    test = get_object_or_404(Tests, pk=question.for_test.pk)

    context = {'question': question}
    queryset = Answers.objects.filter(for_question=pk)

    if request.method == 'POST':
        formset = AnswersFormset(request.POST, queryset=queryset)
        i = 0
        for form in formset:
            if form['answer_is_true'].data == True:
                i += 1

            if i >= 2:
                print('верным должен быть только 1 вопрос')
                return HttpResponseRedirect(reverse('staff:add_answer_to_question', args=[pk]))

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('staff:test_questions', args=[test.pk]))
        else:
            print('dfsgdfhfg')
    else:
        formset = AnswersFormset(queryset=queryset, initial=[{'for_question': question.pk}])
        context['formset'] = formset
    return render(request, 'staff/add_answer_to_question.html', context)

# РАботает
def delete_test(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    # theme = get_object_or_404(ThemeOfTests, pk=test.theme_id.pk)
    office_item = Office.objects.filter(user_id=request.user, tests_id=pk)
    if request.method == 'POST':
        test.delete()
        if  office_item:
            office_item.delete()
        return HttpResponseRedirect(reverse('tests:tests'))
    # context = {'test': test}
    # return render(request, 'staff/test_confirm_delete.html', context)

# РАботает
def delete_answer(request, pk):
    answer = get_object_or_404(Answers, pk=pk)
    question = get_object_or_404(TestQuestions, pk=answer.for_question.pk)
    test = get_object_or_404(Tests, pk=question.for_test.pk)
    if request.method == 'POST':
        answer.delete()
        return HttpResponseRedirect(reverse('staff:test_questions', args=[test.pk]))

    # context = {
    #     'answer': answer,
    #     'test': test,
    # }
    # return render(request, 'staff/answer_confirm_delete.html', context)

# РАботает
def delete_question(request, pk):
    question = get_object_or_404(TestQuestions, pk=pk)

    test = get_object_or_404(Tests, pk=question.for_test.pk)
    if request.method == 'POST':
        question.delete()
        return HttpResponseRedirect(reverse('staff:test_questions', args=[test.pk]))

    context = {
        'question': question,
        'test': test,
    }
    return render(request, 'staff/question_confirm_delete.html', context)

# РАботает
def edit_test_name(request, pk):
    test_edit = get_object_or_404(Tests, pk=pk)
    theme = get_object_or_404(ThemeOfTests, pk=test_edit.theme_id.pk)

    if request.method == 'POST':
        test_edit_form = TestForm(request.POST, instance=test_edit)
        if test_edit_form.is_valid():
            test_edit_form.save()
            return HttpResponseRedirect(reverse('staff:tests_by_theme', args=[test_edit.theme_id.pk]))

    else:

        test_edit_form = TestForm(initial={'theme_id': theme.pk}, instance=test_edit)

    context = {
        'test': test_edit,
        'test_update_form': test_edit_form,
    }
    print(test_edit_form)
    return render(request, 'staff/test_name_update.html', context)


def send_to_moderate(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    test.moderate = 'OM'
    test.save()
    return HttpResponseRedirect(reverse('staff:tests'))
