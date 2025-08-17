from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "ccounts/login.html"

class CustomLogoutView(LogoutView):
    template_name = "account/logout.html"

@login_required
def profile(request):
    return render(request, "accounts/profile.html")
    
