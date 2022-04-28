from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from myapp.form import SignupForm


def home(request):
    return render(request, 'myapp/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=pwd)
            login(request, user)
            return redirect('home')

    form = SignupForm
    return render(request, 'registration/signup.html', {'form': form})
