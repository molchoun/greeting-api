from django.db import models
from django.conf import settings


class Greeting(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from user: {self.message}"
