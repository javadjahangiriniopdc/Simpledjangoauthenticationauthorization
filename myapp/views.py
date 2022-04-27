from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')

def signup(request):
    return render(request,'registration/signup.html')