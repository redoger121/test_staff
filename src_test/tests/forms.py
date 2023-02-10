from django import forms
from .models import *
from django.forms import modelformset_factory


# TestForm=modelformset_factory(
#     Tests, fields='__all__', extra=1
# )

class TestForm(forms.ModelForm):
    # theme_id=forms.F(label='Название теста', widget=forms.HiddenInput())
    class Meta:
        model = Tests
        fields = {'name', 'theme_id', 'image', 'creator', 'description'}

        widgets = {

            'name': forms.Textarea(attrs={'class': 'test__input', 'placeholder': 'Введите название теста'}),
            'theme_id': forms.Select(
                attrs={'class': 'js-example-basic-single row__value', 'placeholder': 'Введите название теста'}),
            'image': forms.FileInput(),
            'creator': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'class': 'test__input', 'placeholder': 'Введите описание теста'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_neme, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
    #         field.help_text = ''
    # if field_neme=='theme_id':
    #     field.widget=forms.HiddenInput()


# class TestsForm(forms.ModelForm):
#     class Meta:
#         model=Tests
#         fields='__all__'

# QuestionsForm=modelformset_factory(
#     TestQuestions, fields='__all__', extra=1
# )

class QuestionsForm(forms.ModelForm):
    class Meta:
        model = TestQuestions
        fields = '__all__'


QuestionFormSet = modelformset_factory(TestQuestions, fields='__all__',
                                       widgets={'for_test': forms.HiddenInput(),
                                                'name': forms.Textarea(attrs={'class': 'test__question-input--big',
                                                                              'placeholder': 'Введите вопрос'})},
                                       extra=1)
QuestionFormSet_optional = modelformset_factory(TestQuestions, fields='__all__',
                                                widgets={'for_test': forms.HiddenInput(),
                                                         'name': forms.Textarea(
                                                             attrs={'class': 'test__input',
                                                                    'placeholder': 'Введите вопрос'}, )},
                                                extra=0)

AnswersFormset = modelformset_factory(Answers, fields='__all__',
                                      extra=1,
                                      widgets={
                                          'name': forms.Textarea(
                                              attrs={'class': 'test__question-input--big  answer__input'}),
                                          'for_question': forms.HiddenInput(),
                                          'answer_is_true': forms.CheckboxInput(attrs={'class': 'question__input'}),
                                      }, labels={'answer_is_true': ''}, )

AnswersFormset_optional = modelformset_factory(Answers, fields='__all__',
                                               labels={'answer_is_true': 'Ответ является верным?'},
                                               widgets={
                                                   'name': forms.Textarea(attrs={'class': 'test__input'}),
                                                   'for_question': forms.HiddenInput(),
                                                   'answer_is_true': forms.CheckboxInput(
                                                       attrs={'class': 'question__input'})},
                                               extra=0)


class TestName(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'class': 'test__input',
                                                        'placeholder': 'Введите логин пользователя'}), label='')


ThemeFormset = modelformset_factory(ThemeOfTests, fields='__all__', extra=0, widgets={
    'name': forms.TextInput(attrs={'class': 'test-search'}),
    'image': forms.FileInput(attrs={'class': 'left-input'})
})


class FindTest(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'find-input test-sort__find-input',
                                                         'placeholder': 'Введите название теста'}), label='')
