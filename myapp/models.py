from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=25)
    family = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name + "-" + self.family
