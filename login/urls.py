from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.login_page, name="login_page"), # Get page
    re_path(r'^user/profile/\w+', views.profile_page), # Get page
    re_path(r'^user/get_badges/', views.getUserBadges, name='getBadges'), # Post only
    re_path(r'^user/create_account/', views.createAccount, name="createAccount"), # Post only
    re_path(r'^user/search_user/', views.searchUser, name='searchUser'), # Post only
    re_path(r'^user/login/', views.login, name='login'), # Post only
    re_path(r'^user/\w+', views.landing_page), # Get page, user/123
    re_path(r'^user/', views.getUser, name='user'), # Post only user/123/
]