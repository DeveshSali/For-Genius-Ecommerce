from django.db import models
from product.models import Product
from user.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator 

# Create your models here.
class Order(models.Model):
    # order details
    order_id = models.IntegerField(null = False, blank = False)
    user_email = models.ForeignKey(User, on_delete=CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    # product details
    product_name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(validators=[MinValueValidator(0)], default=0.01, max_digits=20, decimal_places=2)
    product_id = models.IntegerField(null = False, blank = False)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    # address detail
    name = models.CharField(max_length=255)
    address_line = models.CharField(max_length=255)
    post_code = models.IntegerField(validators=[MinValueValidator(1)])
    suburb = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.IntegerField(validators=[MinValueValidator(1)])
    
    class Meta:

        db_table = 'order'

        unique_together = ("order_id", "product_id", "user_email")

class Cart(models.Model):
    user_email = models.ForeignKey(User, on_delete=CASCADE)
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:

        db_table = 'cart'

        unique_together = ("user_email", "product_id")
