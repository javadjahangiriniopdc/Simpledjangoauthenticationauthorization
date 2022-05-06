from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=25)
    family = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name + "-" + self.family

    # add_person,Can add person
    # change_person,Can change person
    # delete_person,Can delete person
    # view_person,Can view person
    # By default add permission to auth_permission on migrate model
    class Meta:
        permissions = [
            {'custom_person_permission', 'custom person permission'}
        ]
    # please don't forget make migration and migrate for insert custom_person_permission in to auth_permission table
    # and login in admin panel and assign custom_person_permission to user for test
