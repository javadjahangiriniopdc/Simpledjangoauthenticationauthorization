from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from myapp.form import SignupForm
from myapp.models import Person


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


@login_required()
@permission_required('myapp.custom_person_permission', raise_exception=True)
def person(request):
    persons = Person.objects.all()
    return render(request, 'myapp/person.html', {'persons': persons})
