from django.shortcuts import render

# Create your views here.
from myapp.form import SignupForm


def home(request):
    return render(request, 'myapp/index.html')


def signup(request):
    form = SignupForm
    return render(request, 'registration/signup.html', {'form': form})
