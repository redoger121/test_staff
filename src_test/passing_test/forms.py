from django import forms
from django.forms import modelformset_factory

from passing_test.models import PassedAnswers
from user_office.models import Url

class AnswerPassForm(forms.ModelForm):
    model = PassedAnswers



AnswerFormSet = modelformset_factory(PassedAnswers, fields='__all__', form=AnswerPassForm, extra=0,
                                     widgets={'real_answer': forms.HiddenInput(),
                                              'for_question': forms.HiddenInput(),
                                              'name': forms.HiddenInput(),
                                              'answer_is_true': forms.CheckboxInput(attrs={'class': 'question__input'}),
                                              })


UrlsFormSet=modelformset_factory(Url, fields='__all__', extra=0,  widgets={
    'url_data': forms.Textarea(attrs={'class': 'vacancy__input'}),
    'theme':forms.HiddenInput()}, labels={'url_data': ''})