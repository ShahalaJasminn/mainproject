from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[

    path('',views.index),
    path('',views.index),
    path('login',views.login),
    path('login_post',views.login_post),
    path('logout',views.logout),
    path('admin_dash',views.admin_dash),
    path('user_dash',views.user_dash),
    path('registration',views.registration),
    path('registration_POST',views.registration_POST),
    path('view_feedback', views.view_feedback),
    path('view_user',views.view_user),
    path('send_feedback',views.send_feedback),
    path('send_feedback_post', views.send_feedback_post),
    path('upload_image',views.upload_image),
    path('uploadimageee',views.uploadimageee),

]