from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog.models import Category, Product
from catalog import models as pmod

@view_function
def process_request(request, product: pmod.Product):
   
    plist = product.image_urls()

    context = {
        'product':  product,
        'plist': plist,
    }

    return request.dmp.render('product.html', context)


@view_function
def tile(request, product: pmod.Product):
    # product = pmod.Product.ojbects.get(id=)

    context = {
        'product':  product,
    }

    return request.dmp.render('product.tile.html', context)


