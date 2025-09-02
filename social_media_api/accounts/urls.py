# from django.urls import path
# from .views import RegisterationView
# from rest_framework.authtoken.views import obtain_auth_token
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome")

# urlpatterns = [
#     path('register/', RegisterationView.as_view(), name='register'),
#     path('login/', obtain_auth_token, name='login' )
# ]


from django.urls import path
from .views import follow_user, unfollow_user
from .views import RegistrationView, ProfileView, CustomLoginView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]
