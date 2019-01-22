from django.db import models
from datetime import datetime

class Ttodo(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    priority = models.IntegerField(default=2)
    published_date = models.DateTimeField(auto_now_add=True)
    def priority_str(self):
        if self.priority == 1:
            return "여유"
        elif self.priority == 2:
            return "보통"
        else:
            return "긴급"
    def deadline_str(self):
        if not self.deadline:
            return ''
        else:
            return datetime.strftime(self.deadline,'%Y-%m-%d')
    def published_str(self):
        return datetime.strftime(self.published_date,'%Y-%m-%d')
    
    def __str__(self):
        return self.title
