from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views.decorators.http import require_POST
from .models import User


def users_list(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if name and email and password:
            User.objects.create(
                name=name,
                email=email,
                password=make_password(password),
            )
        return redirect("/users/")

    users = User.objects.all()
    return render(request, "myapp/users.html", {"users": users})


@require_POST
def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect("users_list")