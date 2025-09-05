# notifications/models.py
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions')
    verb = models.CharField(max_length=255)  # e.g., "liked your post"
    
    # Generic relation to any object (post, comment, etc.)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Optional: track if notification was seen

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.actor} {self.verb} -> {self.recipient}"



# from django.db import models
# # from django.contrib.auth.models import User
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.conf import settings
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey

# # User = get_user_model()
# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# # Create your models here.
# class Notification(models.Model):
#     recipient =  models.ForeignKey(
#     settings.AUTH_USER_MODEL,
#     on_delete=models.CASCADE,
#     related_name="notifications"
# )
#     actor = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="actions"
# )
#     verb = models.CharField(max_length=300)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveBigIntegerField()
#     target = GenericForeignKey("content_type", "object_id")

#     preview_text = models.TextField(blank=True, null=True)
#     target_url = models.URLField(blank=True, null=True)

#     is_read = models.BooleanField(default=False)

#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-created_at"]
    
#     def __str__(self):
#         return f"Notification to {self.recipient} - {self.verb}"
