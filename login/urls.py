from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="login_page"),
    # path('', views.index, name="landing_page"),  # don't go to that page directly
    re_path(r'^user/createaccount/', views.createAccount, name="createAccount"),
    re_path(r'^user/', views.api, name="apicall"),
    re_path(r'^user/login/', views.login, name='login'),
]
