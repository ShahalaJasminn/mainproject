from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[

    path('',views.index),
    path('login',views.login),
    path('login_post',views.login_post),
    path('admin_dash',views.admin_dash),
    path('user_dash',views.user_dash),
    path('registration',views.registration),
    path('registration_POST',views.registration_POST),
    path('view_feedback', views.view_feedback),
    path('view_user', views.view_user),

]