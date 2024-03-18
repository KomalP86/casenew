from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ErrorLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    error_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    screenshot = models.ImageField(upload_to='error_screenshots/')
    video = models.FileField(upload_to='error_videos/', null=True, blank=True)