from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=200)
    
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


class ProductVariant(models.Model):
    """
    This model holds the values for price and combination of attributes
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #variant = models.ManyToManyField(ProductAttribute)
    color = models.CharField(max_length=20, blank=True)
    size = models.CharField(max_length=20, blank=True)
    texture = models.CharField(max_length=20, blank=True)
    price = models.DecimalField(max_digits=25, decimal_places=2)

