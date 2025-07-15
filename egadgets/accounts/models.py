from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product_images')
    options=(
     
    ('SmartPhone', 'SmartPhone'),
    ('Tablet', 'Tablet'),
    ('SmartWatch', 'SmartWatch'),
    ('LapTop', 'LapTop'),
    ('Headphones', 'Headphones'),
    ('Camera', 'Camera'),
    ('GamingConsole', 'Gaming Console'),
    ('Accessories', 'Accessories'),


    )
    category=models.CharField(max_length=100,choices=options)
    def __str__(self) -> str:
        return self.title

class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    datatime=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(default=1)

class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    datatime=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField()
    options=(
        ('OrderPlaced','OrderPlaced'),
        ('Shipped','Shipped'),
        ('OutForDelivery','OutForDelivery'),
        ('Delivered','Delivered'),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=100,default='OrderPlaced',choices=options)
    def __str__(self) -> str:
        return self.product.title