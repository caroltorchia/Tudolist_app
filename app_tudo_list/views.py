from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def home(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "home.html")


@login_required(login_url="register/login")
def dashboard(request):
    return render(request, "dashboard.html")
