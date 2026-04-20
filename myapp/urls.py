from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users_list, name="users_list"),
    path("users/edit/<int:user_id>/", views.edit_user, name="edit_user"),
    path("users/delete/<int:user_id>/", views.delete_user, name="delete_user"),
]
