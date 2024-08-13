from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Choices):
        
        CLOTHES =  'Clothes'
        ELECTRONICS =  'Electronics'
        FURNITURE =  'Furniture'
        BEAUTY =  'Beauty'

class Product(models.Model):
    name=models.CharField(max_length=30,default="",blank=True)
    description=models.TextField(max_length=1000,default="",blank=True)
    price=models.DecimalField(max_digits=7,decimal_places=2,default=0,blank=True)
    brand=models.CharField(max_length=30,default='',blank=True)
    category=models.CharField(max_length=30,choices=Category.choices)
    rating=models.DecimalField(max_digits=3,decimal_places=2,default=0,blank=True)
    stock=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.name=models.name = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

    def __str__(self):
          return self.name