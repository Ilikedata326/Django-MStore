from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from ckeditor.fields import RichTextField 


class Carousel(models.Model):
    image = models.ImageField(upload_to='images/carousel')
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, default='')
    slug = models.SlugField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now=True)

    # Data about data
    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    more_detail = RichTextField(blank=True)
    

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])  
    def __str__(self):
        return self.title
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    added_date = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.product.title
    
class RealImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    added_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.product.title
       

class Video(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', blank=True) 

    def __str__(self):
        return self.product.title  