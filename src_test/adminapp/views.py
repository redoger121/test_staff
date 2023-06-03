from django import forms
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from tests.models import *
from tests.forms import TestForm, ThemeFormset
from authapp.models import TestingUser
from authapp.forms import TestingUserRegisterForm
from adminapp.forms import TestingUserAdminEditForm, AddURL, FindUsers, ThemeForms
from user_office.models import Url, Vacancy
from passing_test.forms import UrlsFormSet


# Create your views here.

# список пользователей не используется
# class TestingUserListView(ListView):
#     model = TestingUser
#     template_name = 'adminapp/users.html'
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)



# список пользователей с поиском (используется)
@user_passes_test(lambda u: u.is_superuser)
def testing_users(request):

    object_list = TestingUser.objects.all()
    if request.method == "POST":
        find_form = FindUsers(request.POST)
        users_for_find=find_form['name'].data
        print(users_for_find)

        object_list=TestingUser.objects.filter(username__contains=users_for_find)

        context = {'object_list': object_list, 'find_form': find_form}
        return render(request, 'adminapp/users.html', context)
    else:
        find_form = FindUsers()
        context = {'object_list': object_list, 'find_form': find_form}

        return render(request, 'adminapp/users.html', context)



#главная страницв админки (исопльзуется)
@user_passes_test(lambda u: u.is_superuser)
def admin_panel(request):
    themes = ThemeOfTests.objects.all()
    tests = Tests.objects.filter(moderate='OM')



    if request.method=='POST':
        form = ThemeForms(request.POST, request.FILES)
        themes_form=ThemeFormset(request.POST, request.FILES)

        for form in themes_form:
            if form.is_valid():
                form.save()


                return HttpResponseRedirect(reverse('admin:admin_panel'))

        if form.is_valid():
            theme=ThemeOfTests(name=form['name'].data, image=form['image'].data)

            theme.save()

            print(form['name'].data)
            theme=ThemeOfTests.objects.get(name=form['name'].data)
            url=Url(theme_id=theme.pk)
            url.save()

            return HttpResponseRedirect(reverse('admin:admin_panel'))
        else:
            print('что то пошло не так')
            print(form['image'].data)
    else:
        form=ThemeForms()
        themes_form=ThemeFormset()
    context = {
        'themes_form': themes_form,
        'form':form,
        'themes': themes,
        'tests': tests,
    }


    return render(request, 'adminapp/admin_panel.html', context)



#создание пользователя из админки, в новой версии еще не реализовано
@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = TestingUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = TestingUserRegisterForm()

    context = {
        'update_form': user_form,
    }
    return render(request, 'adminapp/user_update.html', context)



#редактирование пользователя (используется)
@user_passes_test(lambda u: u.is_superuser)
def update_user(request, pk):
    edit_user = get_object_or_404(TestingUser, pk=pk)
    if request.method == 'POST':
        edit_form = TestingUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = TestingUserAdminEditForm(instance=edit_user)
    context = {
        'edit_form': edit_form,
    }
    return render(request, 'adminapp/user_update.html', context)



#удаление пользователя требуется доработка
@user_passes_test(lambda u: u.is_superuser and u.is_staff)
def user_delete(request, pk):
    user = get_object_or_404(TestingUser, pk=pk)

    if request.method == 'POST':
        # user.is_active = False
        # user.save()
        user.delete()
        return HttpResponseRedirect(reverse('admin:users'))
    context = {
        'user_to_delete': user,
    }
    return render(request, 'adminapp/user_delete.html', context)

#список тем (в новой версии не используется)
def themes(request):
    themes_list = ThemeOfTests.objects.all()

    context = {
        'themes_list': themes_list
    }
    return render(request, 'adminapp/themes_list.html', context)




#создание тем используется другая реализация
class ThemeCreateView(CreateView):
    model = ThemeOfTests
    template_name = 'adminapp/theme_update.html'
    success_url = reverse_lazy('admin:themes')
    fields = '__all__'

#редактирование тем используется другая реализация
class ThemeUpdateView(UpdateView):
    model = ThemeOfTests
    template_name = 'adminapp/theme_update.html'
    success_url = reverse_lazy('admin:themes')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование тем'
        return context


#удаление тем (ожидает обновления)
class ThemeDeleteView(DeleteView):
    model = ThemeOfTests
    template_name = 'adminapp/theme_delete.html'
    success_url = reverse_lazy('admin:themes')



def theme_delete(request, pk):
    theme=get_object_or_404(ThemeOfTests, pk=pk)
    theme.delete()
    return HttpResponseRedirect(reverse('admin:admin_panel'))

    # def form_valid(self, form):
    #     self.object=self.get_object()
    #     success_url=self.get_success_url()
    #     self.object.is_active=False
    #     self.object.save()
    #     return HttpResponseRedirect(success_url)



# тесты по выбранной теме (ожидает обновления)
def tests_by_theme(request, pk):
    theme = get_object_or_404(ThemeOfTests, pk=pk)
    tests = Tests.objects.filter(theme_id=pk)

    context = {
        'theme': theme,
        'tests': tests,
    }
    return render(request, 'adminapp/tests_by_theme.html', context)

# детальное представление теста, скорее всего подлежит удалению
def tests_questions(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    context = {
        'test': test,
    }
    questions = TestQuestions.objects.filter(for_test=pk)

    context['questions'] = questions

    answ = []
    for item in questions:
        answ.append(item.pk)

    answers = Answers.objects.filter(for_question__in=answ)

    context.update({'answers': answers})
    return render(request, 'adminapp/tests_detail.html', context)


# создание теста будет удалено или заменено
def test_create(request, pk):
    them = get_object_or_404(ThemeOfTests, pk=pk)
    context = {}
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        test_name = test_form['name'].data
        test_creator = test_form['creator'].data
        test_them = test_form['theme_id'].data
        test_object = Tests.objects.filter(name=test_name, creator=test_creator, theme_id=test_them)
        if test_object.count() > 0:
            print('у вас уже есть такой тест')
            return HttpResponseRedirect(reverse('admin:test_create', args=[pk]))
        if test_form.is_valid():
            test_form.save()
            test_object = Tests.objects.get(name=test_name, creator=test_creator, theme_id=test_them)
            context['name'] = test_object

    else:
        test_form = TestForm(initial={'theme_id': them, 'creator': request.user})

    context['test_form'] = test_form
    return render(request, 'adminapp/test_create.html', context)


# добавление вопросов к тесту будет удалено или заменено
def add_questions_to_test(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    # queryset = TestQuestions.objects.filter(for_test=pk)
    context = {
        'test': test,
    }
    QuestionFormSet = modelformset_factory(TestQuestions, fields='__all__',
                                           widgets={'for_test': forms.HiddenInput()}, extra=1)
    if request.method == 'POST':
        formset = QuestionFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            context['test_formset'] = formset
            return HttpResponseRedirect(reverse('admin:tests_questions', args=[test.pk]))


    else:
        formset = QuestionFormSet(queryset=TestQuestions.objects.none(), initial=[{'for_test': test.pk}])
        context['test_formset'] = formset
    return render(request, 'adminapp/test_update.html', context)


# добовление ответов к тесту будет удалено или заменено
def add_answers_to_question(request, pk):
    question = get_object_or_404(TestQuestions, pk=pk)
    test = get_object_or_404(Tests, pk=question.for_test.pk)

    context = {'question': question}
    queryset = Answers.objects.filter(for_question=pk)
    if queryset:
        AnswersFormset = modelformset_factory(Answers, fields='__all__',
                                              extra=1)
    else:
        AnswersFormset = modelformset_factory(Answers, fields='__all__',
                                              extra=1)
    if request.method == 'POST':
        formset = AnswersFormset(request.POST, queryset=queryset)
        i = 0
        for form in formset:
            if form['answer_is_true'].data == True:
                i += 1

            if i >= 2:
                print('верным должен быть только 1 вопрос')
                return HttpResponseRedirect(reverse('admin:add_answer_to_question', args=[pk]))

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('admin:tests_questions', args=[test.pk]))
        else:
            print('dfsgdfhfg')
    else:
        formset = AnswersFormset(queryset=queryset, initial=[{'for_question': question.pk}])
        context['formset'] = formset
    return render(request, 'adminapp/add_answer_to_question.html', context)


def delete_test(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    theme = get_object_or_404(ThemeOfTests, pk=test.theme_id.pk)
    if request.method == 'POST':
        test.delete()
        return HttpResponseRedirect(reverse('admin:tests_by_theme', args=[theme.pk]))
    context = {'test': test}
    return render(request, 'adminapp/test_confirm_delete.html', context)


def delete_answer(request, pk):
    answer = get_object_or_404(Answers, pk=pk)
    question = get_object_or_404(TestQuestions, pk=answer.for_question.pk)
    test = get_object_or_404(Tests, pk=question.for_test.pk)
    if request.method == 'POST':
        answer.delete()
        return HttpResponseRedirect(reverse('admin:tests_questions', args=[test.pk]))

    context = {
        'answer': answer,
        'test': test,
    }
    return render(request, 'adminapp/answer_confirm_delete.html', context)


def delete_question(request, pk):
    question = get_object_or_404(TestQuestions, pk=pk)
    test = get_object_or_404(Tests, pk=question.for_test.pk)
    if request.method == 'POST':
        question.delete()
        return HttpResponseRedirect(reverse('admin:tests_questions', args=[test.pk]))

    context = {
        'question': question,
        'test': test,
    }
    return render(request, 'adminapp/question_confirm_delete.html', context)


def edit_test_name(request, pk):
    test_edit = get_object_or_404(Tests, pk=pk)
    theme = get_object_or_404(ThemeOfTests, pk=test_edit.theme_id.pk)

    if request.method == 'POST':
        test_edit_form = TestForm(request.POST, instance=test_edit)
        if test_edit_form.is_valid():
            test_edit_form.save()
            return HttpResponseRedirect(reverse('admin:tests_by_theme', args=[test_edit.theme_id.pk]))

    else:

        test_edit_form = TestForm(initial={'theme_id': theme.pk}, instance=test_edit)

    context = {
        'test': test_edit,
        'test_update_form': test_edit_form,
    }
    print(test_edit_form)
    return render(request, 'adminapp/test_name_update.html', context)


def list_of_tests_to_moderate(request):
    tests = Tests.objects.filter(moderate='OM')

    context = {

        'tests': tests,
    }
    return render(request, 'adminapp/list_of_tests_to_moderate.html', context)


def moderate_test(request, pk):
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
    return render(request, 'adminapp/moderate_test.html', context)


def approve_test(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    test.moderate = 'MO'
    test.save()
    return HttpResponseRedirect(reverse('admin:admin_panel'))


def decline_test(request, pk):
    test = get_object_or_404(Tests, pk=pk)
    test.moderate = 'RE'
    test.save()
    return HttpResponseRedirect(reverse('admin:admin_panel'))


def show_parsers_url(request):
    urls = Url.objects.all()
    themes=ThemeOfTests.objects.all()
    vacinsies_list=[]

    for theme in themes:
        vacancies=len(Vacancy.objects.filter(theme=theme.pk))
        vacancies_dict={"theme": theme.pk, "vacancies_num":vacancies}
        vacinsies_list.append(vacancies_dict)

    if request.method=='POST':
        urls_form = UrlsFormSet(request.POST)

        for form in urls_form:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:show_parsers_url'))
    else:
        urls_form=UrlsFormSet()

    context = {
        'urls_form':urls_form,
        'vacinsies_list':vacinsies_list,
        'themes':themes,
        'urls': urls
    }
    return render(request, 'adminapp/parsers_urls.html', context)


def add_urls_to_parsers(request, pk):
    theme = get_object_or_404(ThemeOfTests, pk=pk)

    if request.method == 'POST':
        form = AddURL(request.POST, )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:show_parsers_url'))

    else:
        form = AddURL(initial={'theme': theme.pk})

    context = {
        'form': form,
    }
    return render(request, 'adminapp/add_url.html', context)


def delete_url(request, pk):
    urls = get_object_or_404(Url, pk=pk)
    if request.method == 'POST':
        urls.delete()
        return HttpResponseRedirect(reverse('admin:show_parsers_url'))
    context = {'url': urls}
    return render(request, 'adminapp/url_confirm_delete.html', context)
