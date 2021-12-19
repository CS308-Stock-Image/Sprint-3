from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.forms.fields import BooleanField
from django_countries.fields import CountryField


# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    category_name=models.TextField()
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    price= models.IntegerField( default=0)
    uploaded_by=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    favorite=models.ManyToManyField(User,related_name='favorite', blank=True )
    
    
    

    def __str__(self):
        return self.description


class CheckoutAddress(models.Model):
    item = models.ForeignKey(Photo,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class ShopCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    product=models.ForeignKey(Photo,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=0)
    ordered=BooleanField(required=False)
    checkout_address=models.ForeignKey(CheckoutAddress,on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.product.title
    @property
    def price(self):
        return(self.product.price)
    



class Follow(models.Model):
    username=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    follows= models.ManyToManyField(User,related_name='follows', blank=True )



