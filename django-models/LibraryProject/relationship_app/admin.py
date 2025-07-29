# from django.contrib import admin

# # Register your models here.


from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Admin"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')
