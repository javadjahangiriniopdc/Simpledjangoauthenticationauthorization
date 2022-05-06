from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('person', views.person, name='person')
]
