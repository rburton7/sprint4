from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django import forms
from datetime import datetime
from decimal import Decimal 
@view_function
def process_request(request):
    cart = request.user.get_shopping_cart()
    cart.save()

    form = CheckoutForm()
    stripeTotal = int(cart.total * Decimal(100.00))
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        form.sale = request.user.get_shopping_cart()
        if form.is_valid():
            #clean method finalizes sale
            return HttpResponseRedirect('/catalog/receipt/{}/'.format(form.sale.id))
    return request.dmp.render('checkout.html',{
        'cart' : cart,
        'form' : form,
        'stripeTotal' : stripeTotal,
    })

class CheckoutForm(forms.Form):
    address = forms.CharField(label='Shipping Address')
    city = forms.CharField(label='Shipping City')
    state = forms.CharField(label = 'Shipping State')
    zipcode = forms.CharField(label = 'Shipping Zip')

    #Stripe widget sends user info, card info over to Stripe, stripe returns a token and puts it in our form field
    #because we have a field called exactly what it needs 'stripeToken'
    stripeToken = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        try:
            self.sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))
        #do I need a return statement here?
        #ie return self.cleaned_data