from django.db import models

# Create your models here.

class Book(models.Model):
    CATEGORY =(
        ('Love','Love'),
        ('Scientific','Scientific'),
        ('Action','Action'),
        ('GK','GK')
    )
#   brand= models.ForeignKey(Registerpage,null=True, on_delete=models.CASCADE)
#    brand= models.CharField(max_length=40, null=True)
    bname = models.CharField(max_length=40, null=True)
    bauthor = models.CharField(max_length=40, null=True)
    quantity = models.CharField(max_length=40,null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250,null=True)
    category = models.CharField(max_length=40,null=True,choices=CATEGORY)
    #date = models.DateTimeField(auto_now_add=True,null=True)



    def __str__(self):
        return self.name



