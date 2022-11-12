from django.contrib import admin
from django.urls import include, path
from . import views
from django.http import HttpResponse
urlpatterns = [
   
    path('', views.home,name="homepage"),
    path('signup',views.signup,name="signup"),
    path('userlogin',views.userlogin,name="login"),
    path('signout',views.signout,name="signout")
]