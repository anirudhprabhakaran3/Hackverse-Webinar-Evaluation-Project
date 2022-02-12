from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Submission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    submission_url = models.CharField(max_length=100, blank=True)
    marks = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username