from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from authapp.models import TestingUser, TestingUserProfile
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _




class UserCreatie(forms.ModelForm):
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"password__input","autocomplete": "new-password", "placeholder":"Пароль"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"class":"password__input","autocomplete": "new-password", "placeholder":"Повторите пароль"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user






class TestingUserRegisterForm(UserCreatie):
    class Meta:
        model = TestingUser
        fields = (
            'username', 'password1', 'password2',
            'email',
        )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Логин'}),
            'password1': forms.TextInput(attrs={'class': 'password__input', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email адрес'}),

        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
    #         field.help_text = ''


class TestingUserEditForm(UserChangeForm):
    class Meta:
        model = TestingUser
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'age', 'avatar', 'date_joined', 'password'
        )
        widgets = {

            'username': forms.TextInput(attrs={'class': 'row__value row__value-input'}),
            'first_name': forms.TextInput(attrs={'class': 'row__value row__value-input'}),
            'last_name': forms.TextInput(attrs={'class': 'row__value row__value-input'}),
            'email': forms.EmailInput(attrs={'class': 'row__value row__value-input'}),
            'age': forms.TextInput(attrs={'class': 'row__value row__value-input'}),

            'date_joined': forms.TextInput(attrs={'class': 'row__value row__value-input'}),
            'avatar': forms.FileInput(attrs={'class': 'row__value row__value-input', 'name': 'file[]',
                                             'type': 'file', ' multiple accept': 'image/*'}),
        }


class TestingUserLoginForm(AuthenticationForm):
    class Meta:
        model = TestingUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(TestingUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name=='password':
                field.widget.attrs['class'] = 'form-control password__input'




class TestingUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = TestingUserProfile
        fields = ('aboutMe', 'gender')

        widgets = {

            'aboutMe': forms.Textarea(attrs={'class': 'row__value row__value-textarea'}),
            'gender': forms.Select(attrs={'class': 'row__value  row__value-input'})

        }


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'password__input', 'placeholder': "Старый пароль"})
        self.fields['new_password1'].widget.attrs.update({'class': 'password__input', 'placeholder': "Новый пароль"})
        self.fields['new_password2'].widget.attrs.update({'class': 'password__input', 'placeholder': "Повторите пароль"})

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
