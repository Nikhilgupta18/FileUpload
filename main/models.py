from django.db import models
from django.contrib.auth.models import User





class Document(models.Model):
    description = models.TextField(max_length=255, blank=True)
    video = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
