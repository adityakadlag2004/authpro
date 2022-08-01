from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password= models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name