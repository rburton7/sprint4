from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from account import models as amod
from catalog import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
 
    myproducts = request.user.get_shopping_cart()
    SI = cmod.SaleItem.objects.filter(status = 'A', sale = myproducts)

    context = {
       
       'myproducts' : myproducts,
       'SI' : SI,

    }
    return request.dmp.render('receipt.html', context)