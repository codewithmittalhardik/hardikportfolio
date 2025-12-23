# models.py
from django.db import models

# models.py
class Contact(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(blank=True, null=True) 
    
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name or 'Anonymous'}"