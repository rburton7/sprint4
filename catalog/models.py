from django.db import models
import sprint1.settings as settings



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
        return self.images_url()[0]

    def images_url(self):
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
    
    #this method confuses me...what is it supposed to be doing?
    def image_url(self):
        return settings.STATIC_URL + "catalog/media/products/" + self.filename

        