from django.db import models
from datetime import datetime

class Ttodo(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    priority = models.IntegerField(default=2)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
