from django.urls import path

from .views import follow_users

urlpatterns = [
    path('followusers/', follow_users, name="follow_users"),

    ]
