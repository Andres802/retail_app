from django.db import models


# Create your models here.
class Orders(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  text = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  last_updated = models.DateTimeField(
    auto_now=True,
    null=False,
    blank=False
  )

  class Shipping(models.Model):
    address = models.CharField(
    null=True, 
    blank=False )

    city = models.CharField( 
    null=False, 
    blank=False
    )
    state = models.CharField( 
    max_length=20,  
    null=False,
    blank=False)

    country = models.Charfield( 
    max_digits=10, 
    ecimal_places=2, 
    default=0.00)
    
    cost = models.DecimalField(
    max_digits=10, 
    decimal_places=2, 
    default=0.00)
    

  class Meta:
    db_table = 'Orders'