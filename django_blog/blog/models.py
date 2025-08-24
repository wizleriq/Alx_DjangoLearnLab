from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager 

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    tags = TaggableManager()
    # tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    def __str__(self):
        return self.title
# ✅ Option 2: Use a string reference

# If you want to keep Tag defined below, you can reference it as a string in ManyToManyField:

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
#     tags = models.ManyToManyField("Tag", related_name='posts', blank=True)  # 👈 string ref

#     def __str__(self):
#         return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
# class Tag(models.Model):
#     Tag = models.ForeignKey(Post, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
    