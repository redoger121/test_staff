from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db import  transaction
from django.urls import reverse
from django.contrib import auth
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authapp.models import TestingUser, TestingUserProfile

from .forms import *


def register(request):
    if request.method=='POST':
        register_form=TestingUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form=TestingUserRegisterForm()
    context={'register_form':register_form}
    return render(request, 'authapp/register.html', context)

def login(request):

    login_form=TestingUserLoginForm(data=request.POST or None)
    _next=request.GET.get('next')

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user and user.is_active:
            auth.login(request, user)
            _next=_next or '/'
            return redirect(_next)
    context={
        'login_form':login_form,
        'next':_next
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('tests:main'))


def user_bio(request):

    user_main_info=TestingUser.objects.get(pk=request.user.pk)
    user_other_info=TestingUserProfile.objects.get(user_id=request.user.pk)
    context={
        'user_main_info': user_main_info,
        'user_other_info':user_other_info,
    }
    return render(request, 'authapp/user.html', context)

@transaction.atomic()
def edit(request):
    if request.method=='POST':
        edit_form=TestingUserEditForm(request.POST, request.FILES, instance=request.user)

        profile_form=TestingUserProfileEditForm(request.POST, instance=request.user.testinguserprofile)

        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            profile_form.save()

            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form=TestingUserEditForm(instance=request.user)
        profile_form=TestingUserProfileEditForm(instance=request.user.testinguserprofile)

    context={
        'edit_form':edit_form,
        'profile_form':profile_form,

    }
    return render(request, 'authapp/edit.html', context)






from authapp.forms import MyPasswordChangeForm
class ChangePassword(LoginRequiredMixin,TemplateView):

    def get(self, request, *args, **kwargs):
        form_class = MyPasswordChangeForm

        form = form_class(self.request.user)
        return render(request, 'authapp/change_paasword.html',{'form': form,})

    def post(self, request, *args, **kwargs):
        form_class = MyPasswordChangeForm
        form = form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return HttpResponseRedirect(reverse('auth:logout'))
        else:
            return render(request, 'authapp/change_paasword.html', {'form': form, 'password_changed': False})



