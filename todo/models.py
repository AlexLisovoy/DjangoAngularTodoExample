from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=150)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
