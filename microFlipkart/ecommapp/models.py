from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class UserModel(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=10)
    role=models.CharField(max_length=5)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)





class ProductModel(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


class VariantModel(models.Model):
    name=models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.name

class ProductVariantModel(models.Model):
    """
    This model holds the values for price and combination of attributes
    """
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    VariantModel=models.ForeignKey(VariantModel,on_delete=models.CASCADE)
    VariantValue=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    quantity=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    list_display = ('color', 'size', 'texture', 'price')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.product.name}, {self.VariantModel}, {self.VariantValue}'



class OrderModel(models.Model):
    usermodel=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    price=models.FloatField(default=0)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity_left=models.IntegerField(default=0)
    variant=models.ForeignKey(VariantModel,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,default='PLACED')
    active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


