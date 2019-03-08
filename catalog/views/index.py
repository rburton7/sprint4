from datetime import datetime, timezone
from catalog.models import Category, Product
import math
from django_mako_plus import view_function, jscontext
from django.conf import settings

@view_function
def process_request(request, category: Category=None, page:int=1):
    max_products = 8
    start = (page-1) * max_products

    if category is None:
        products = Product.objects.filter(status='A')
    else:
        products= Product.objects.filter(category=category)

    categories = Category.objects.all()

    context = {
       'categories': categories,
    }
    return request.dmp.render('index.html', context)