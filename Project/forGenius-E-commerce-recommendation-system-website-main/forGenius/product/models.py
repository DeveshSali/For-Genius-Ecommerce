from django.db import models
from django.db.models.deletion import CASCADE
from user.models import Admin
from django.core.validators import MinValueValidator 

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=10000000)
    warranty = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    delivery_date = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    sales_data = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    admin_email = models.ForeignKey(Admin, on_delete=CASCADE)
    price = models.DecimalField(validators=[MinValueValidator(0)], default=0.01, max_digits=20, decimal_places=2)
    picture = models.CharField(max_length=255, blank=True)

class Features(models.Model):
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
    feature = models.CharField(max_length=30)

    class Meta:

        db_table = 'features'

        unique_together = ("product_id", "feature")
