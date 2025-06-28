from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catagery(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE, null=True)
    title = models.CharField( max_length=50)
    
    def __str__(self):
        return self.title
    
class Subcatagery(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE, null=True)
    catagery= models.ForeignKey(Catagery,  on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
    
    