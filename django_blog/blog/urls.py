# from django.urls import path
# from .views import register, CustomLoginView, CustomLogoutView, profile

# urlpatterns = [
#     path('register/', register, name='register'),
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('logout/', CustomLogoutView.as_view(), name='logout' ),
#     path('profile/', profile, name='profile')
# ]

from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, profile
from .views import ( PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView)

urlpatterns = [
    # Post CRUD URLs
    # # path("token/", obtain_auth_token, name="api_token_auth"),
    # path("posts/", PostListView.as_view(), name='post-list'),
    # path("post/new/", PostCreateView.as_view(), name='post-create'),
    # path("post/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    # path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    # path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
    
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    
    # Auth & profile URLs
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]
