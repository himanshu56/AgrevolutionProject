from django.shortcuts import render

# Create your views here.

from products.models import Product, ProductVariant

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_products = Product.objects.all().count()
    
    # Available books (status = 'a')
    num_varients_available = 1 #ProductVariant.objects.filter(status__exact='a').count()
    
    context = {
        'num_products': num_products,
        'num_varients_available': num_varients_available,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)