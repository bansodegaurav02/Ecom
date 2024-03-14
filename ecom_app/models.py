from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class category(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/')

    
    def __str__(self):
        return self.name






class products(models.Model):
    cat=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=2000)
    prize=models.IntegerField()
    images=models.ImageField(upload_to='images/')


    
    





class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.quantity*self.product.prize






class product_rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    info=models.CharField(max_length=300,default=0)
    rating=models.IntegerField(default=0)


Status_choice=(
    ('APPROVED','APPROVED'),
    ('DELIVERD','DELIVERD')
)

class orders_data(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quntity=models.PositiveIntegerField()
    Address=models.TextField()
    status=models.CharField(max_length=100,choices=Status_choice,default='pending')
    total_amount=models.IntegerField()
    fname=models.CharField(max_length=100,default=0)
    
    mobile_no=models.CharField(max_length=100,default=0)
    email=models.EmailField(max_length=100,default=0)
    


