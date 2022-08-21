from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    head0 = models.CharField(max_length=450,default="")
    chead0 = models.CharField(max_length=5050,default="")
    chead1 = models.CharField(max_length=5050,default="")
    chead2 = models.CharField(max_length=5050,default="")
    head1 = models.CharField(max_length=550,default="")
    head2 = models.CharField(max_length=650,default="")
    thumbnail = models.ImageField(upload_to="blog/images",default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.title