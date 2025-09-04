from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()
# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor')
    verb = models.CharField(max_length=300)
    target = GenericForeignKey("content_type", "object_id")

    preview_text = models.TextField(blank=True, null=True)
    terget_url = models.URLField(blank=True, null=True)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Mets:
        ordering = ["created_at"]
    
    def __str__(self):
        return f"Notification to {self.recipient} - {self.verb}"
