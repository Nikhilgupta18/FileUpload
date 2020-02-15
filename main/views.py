from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . import models
from .forms import SignUpForm, DocumentForm
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)


def index(request):
    files = models.Document.objects.all()
    context = {
        'files': files,
    }
    return render(request, 'index.html', context)


# Create your views here.
class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    next_page = '/'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'uploaded.html', {
        'form': form
    })

