from django import forms


from authapp.models import TestingUser
from authapp.forms import TestingUserEditForm
from tests.models import *
from user_office.models import Url

class TestingUserAdminEditForm(TestingUserEditForm):
    class Meta:
        model=TestingUser

        fields = (
            'username', 'first_name',
            'email', 'age', 'avatar',

            'user_permissions', 'last_name', 'is_staff',
            'is_active', 'date_joined',
        )
        widgets = {

            'username': forms.TextInput(attrs={'class': 'row__value row__value-input'}),
            'first_name': forms.TextInput(attrs={'class': 'row__value  row__value-input'}),
            'last_name': forms.TextInput(attrs={'class': 'row__value  row__value-input'}),
            'email': forms.EmailInput(attrs={'class': 'row__value  row__value-input'}),
            'age': forms.TextInput(attrs={'class': 'row__value  row__value-input'}),
            'date_joined': forms.TextInput(attrs={'class': 'row__value  row__value-input'}),
            'avatar': forms.FileInput(attrs={'class': 'row__value  row__value-input'}),


            'user_permissions': forms.SelectMultiple(attrs={'class': 'row__value  row__value-textarea'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'question__input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'question__input'}),
            'password':forms.HiddenInput(),





        }



class ListOfThemesAdminEditForm(forms.ModelForm):
    class Meta:
        model=ThemeOfTests
        fields='__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.wodget.attrs['class']='form-control'

class AddURL(forms.ModelForm):



    class Meta:
        model = Url
        fields = '__all__'



class FindUsers(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'find-input test-sort__find-input',
                                                        'placeholder': 'Введите название теста'}), label='')









class ThemeForms(forms.ModelForm):
    # theme_id=forms.F(label='Название теста', widget=forms.HiddenInput())
    class Meta:
        model = ThemeOfTests
        fields = "__all__"

        widgets = {

            'name': forms.TextInput(attrs={'class': 'test-search', 'placeholder': 'Введите название новой темы'}),
            'image': forms.FileInput(),

        }






