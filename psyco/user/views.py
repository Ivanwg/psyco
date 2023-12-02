from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user_to_login = authenticate(username=username, password=raw_password)
            login(request, user_to_login)
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('home')
