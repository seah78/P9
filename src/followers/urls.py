from django.urls import path

from .views import follow_users, delete_follow

urlpatterns = [
    path('followusers/', follow_users, name="follow_users"),
    path('delete_follow/<int:user_id>', delete_follow, name="delete_follow"),

    ]
