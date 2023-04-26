from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator 

# Create your models here.
class User(models.Model):
    user_email = models.EmailField(unique=True, primary_key=True)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=255)

class Admin(models.Model):
    admin_email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=255)

class Interest(models.Model):
    user_email = models.ForeignKey(User, on_delete=CASCADE)
    interests = models.CharField(max_length=255)

    class Meta:

        db_table = 'interest'

        unique_together = ("user_email", "interests")
        
class Search_history(models.Model):
    user_email = models.ForeignKey(User, on_delete=CASCADE)
    search = models.CharField(max_length=255)
    
class Address_book(models.Model):
    user_email = models.ForeignKey(User, on_delete=CASCADE)
    address_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address_line = models.CharField(max_length=255)
    post_code = models.IntegerField(validators=[MinValueValidator(1)])
    suburb = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.IntegerField(validators=[MinValueValidator(1)])
