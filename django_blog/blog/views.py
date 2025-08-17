from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

# Registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in after registration
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

# Login view
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

# Logout view
class CustomLogoutView(LogoutView):
    template_name = "accounts/logout.html"

# Profile view
@login_required
def profile(request):
    return render(request, "accounts/profile.html")
