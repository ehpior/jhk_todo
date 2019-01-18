from django.db import models

class Ttodo(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
