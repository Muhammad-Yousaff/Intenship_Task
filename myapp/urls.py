from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.users_list, name="users_list"),
    path("users/delete/<int:user_id>/", views.delete_user, name="delete_user"),
]
