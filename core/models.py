from django.db import models
from django.contrib.auth.models import User

class db(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name