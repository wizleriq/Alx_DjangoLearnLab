from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikeView, UnlikeView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns =[
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path("posts/<int:pk>/like/", LikeView.as_view(), name='Like-post'),
    path("posts/<int:pk>/unlike", UnlikeView.as_view, name='Un-like-post')
    
]



# Checks for “Add URL patterns in posts/urls.py for liking and unliking posts, such as /posts/int:pk/like/ and /posts/int:pk/unlike/.” task

# posts/urls.py doesn't contain: ["<int:pk>/unlike/"]
