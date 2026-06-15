from django.db import models

class db(models.Model):
    name=models.CharField(max_length=100)
    age=models.SmallIntegerField()
    gender=models.CharField(max_length=20)

    def __str__(self):
        return self.name
