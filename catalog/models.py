from django.db import models
import sprint1.settings as settings
from decimal import Decimal
import stripe
from catalog import models as cmod
from datetime import datetime


TAX_RATE = Decimal("0.05")

class Sale(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    purchased = models.DateTimeField(null=True, default=None)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    charge_id = models.TextField(null=True, default=None)

    def recalculate(self):
        self.subtotal = Decimal("0.00")
        self.total = Decimal("0.00")
        for sitem in SaleItem.objects.filter(sale=self, status='A'):
            self.subtotal += sitem.quantity * sitem.price
        
        self.tax = (self.subtotal * TAX_RATE)
        self.total = (self.subtotal + self.tax)
       

    def finalize(self, stripeToken):
        saleitems = SaleItem.objects.filter(status='A', sale=self)
        # Ensure this sale isn't already finalized (purchased should be None)
        if self.purchased == None :
            # Check product quantities one more time
            for si in saleitems:
                si.product.quantity <= si.quantity
            self.recalculate()
            #token = request.form['stripeToken'] #goes in clean method of form
            charge = stripe.Charge.create(
                amount= int(round((self.total * Decimal("100.0")),2)),
                currency='usd',
                description='Example charge',
                source=stripeToken,
            )
            # Set purchased=now and charge_id=the id from Stripe
            self.purchased = datetime.now()
            self.charge_id = charge['id']
            self.save()
    
    

class SaleItem(models.Model):
    STATUS_CHOICES = [
        ( 'A', 'Active' ),
        ( 'D', 'Deleted' ),
    ]
    status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))

class Meta:
    ordering = [ 'product__name' ]


class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    Active = 'A'
    Inactive = 'I'

    STATUS_CHOICES = (
        (Active, 'A'),
        (Inactive, 'I'),
    )
    status = models.TextField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='A',
        db_index = True
    )
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    reorder_trigger = models.IntegerField(default=2)
    reorder_quantity = models.IntegerField(default=5)
    

    def image_url(self): 
        return self.image_urls()[0]

    def image_urls(self):
        prodimgs= ProductImage.objects.filter(product = self)
        urls = []
        for p in prodimgs :
            urls.append(p.image_url())
        if len(prodimgs) == 0 :
            urls.append(settings.STATIC_URL + "catalog/media/products/notfound.jpg")
        return urls
 


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filename = models.TextField()
    
 
    def image_url(self):
        return settings.STATIC_URL + "catalog/media/products/" + self.filename

        