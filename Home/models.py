from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password= models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name



class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=300)
    desc=models.CharField(max_length=700)
    pub_date=models.DateField()
    
