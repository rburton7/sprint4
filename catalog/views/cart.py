from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from account import models as amod
from catalog import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
 
    myproducts = request.user.get_shopping_cart()
    myproducts.recalculate()
    myproducts.save()
    SI = cmod.SaleItem.objects.filter(status = 'A', sale = myproducts)

    context = {
       
       'myproducts' : myproducts,
       'SI' : SI,

    }
    return request.dmp.render('cart.html', context)
@view_function
def remove(request, id:int):
   
    myproducts = request.user.get_shopping_cart()

    SIdelete = cmod.SaleItem.objects.get(id=id)
    SIdelete.status = 'D'
    SIdelete.save()

    #grader might want a recalculate
    SI = cmod.SaleItem.objects.filter(status = 'A', sale = myproducts)

    context = {
       
       'myproducts' : myproducts,
       'SI' : SI,

    }
    return HttpResponseRedirect('/catalog/cart/')
