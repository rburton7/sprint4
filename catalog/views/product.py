from django.conf import settings
from django_mako_plus import view_function, jscontext, RedirectException
from datetime import datetime, timezone
from catalog.models import Category, Product
from catalog import models as pmod
from django import forms
from django.http import HttpResponse, HttpResponseRedirect

@view_function
def process_request(request, product: pmod.Product):
   
    plist = product.image_urls()
    if request.method=='POST':
        form = PurchaseForm(request.POST)
        form.user = request.user
        form.product = product
        form.sale=request.user.get_shopping_cart()

        if form.is_valid():
            form.commit(product)
            PurchaseForm(request, form.user)

            return HttpResponseRedirect(f'/catalog/cart/{request.user.get_shopping_cart().id}')

    else:
        form = PurchaseForm()
    

    context = {
        'form' : form,
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




class PurchaseForm(forms.Form):
    #give TextInput a label?
    quantity = forms.CharField(label='Quantity')
    # product_id = forms.CharField(widget=forms.HiddenInput())
    # product = None
    # user = None

    def clean(self):
        qcart = 0
        saleItem = None
        q = self.cleaned_data.get('quantity')
        mycart = self.sale
        SI = pmod.SaleItem.objects.filter(sale=self.sale)
        for item in SI:
            if self.product == item.product:
                    qcart = item.quantity
        
        print(q)

        if q is None or q =="0":
            raise forms.ValidationError('Quantity must be greater than zero.')

        if self.product.quantity < int(q) + qcart:
            raise forms.ValidationError('Insufficient inventory for this order')



        if self.user.is_authenticated == False:
            raise RedirectException('/account/login')

        # if saleItem is None :
        #     saleItem = pmod.SaleItem()
        #     saleItem.product = self.product
        #     saleItem.sale = self.user.get_shopping_cart()
        #     saleItem.price = pmod.Product.objects.get(pk=self.product.id).price
        
        # saleItem.quantity += self.product.quantity

    def commit(self, prod):
        sale=self.sale
        cart=pmod.SaleItem.objects.filter(sale=self.sale)
        i=0
        for var in cart:
            if var.product==prod and var.status=='A':
                var.quantity+=int(self.cleaned_data.get('quantity'))
                var.save()
                i+=1
        if i==0:
            sItem=pmod.SaleItem()
            sItem.price=prod.price
            sItem.quantity=int(self.cleaned_data.get('quantity'))
            sItem.sale = sale
            sItem.product = prod
            sItem.save()


