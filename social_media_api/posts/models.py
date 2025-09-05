from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,  # references Post model
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

class Like(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='liked_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.user.username} liked {self.post.id}"






# from django.db import models
# from django.conf import settings

# # Create your models here.
# class Post(models.Model):
#     author = models.CharField(max_length=100, on_delete=models.CASCADE, related_name='post')
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    
#     class Comment(models.Model):
#         post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')
#         author = models.ForeignKey(settings.Auth_user_model, on_delete=models.CASCADE, related_name='comments')
#         content = models.TextField()
#         created_at = models.DateTimeField(auto_add_now=True)
#         updated_at = models.DateTimeField(auto_now=True)

#         def __str__(self):
#             return  f"Comment by {self.author} on {self.post}"