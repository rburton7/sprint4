from datetime import datetime, timezone
from catalog.models import Category, Product
import math
from django_mako_plus import view_function, jscontext
from django.conf import settings
from catalog import models as cmod

ITEMS_PER_PAGE = 4

@view_function
def process_request(request, category: Category=None, page:int=1):
       
    if category is None:
        products = Product.objects.filter(status='A')
    else:
        products= Product.objects.filter(category=category)

    numpages = math.ceil(products.count() / ITEMS_PER_PAGE)
    

    products = products[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]

    context = {
       'category': category, 
       'products': products,
       'page': page,
       'numpages': numpages,
    }
    return request.dmp.render('index.html', context)