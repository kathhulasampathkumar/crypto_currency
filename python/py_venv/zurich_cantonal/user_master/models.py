from django.db import models

# Create your models here.

class user_master(models.Model):            
    username   =  models.CharField(max_length=50,null=True)
    contact =    models.CharField(max_length=20,null=True)
    email   =  models.CharField(max_length=50,unique=True)
    city    =   models.CharField(max_length=20,null=True)
    password    =   models.CharField(max_length=50,null=True)
    balance     = models.DecimalField(max_digits=25, decimal_places=8, null=True)
    USER_CHOICES = ( ('user', 'User'),('admin', 'Admin'),('other', 'Other'),    )
    user_type   = models.CharField(max_length=25, default='user', choices=USER_CHOICES)
    # user_type   = models.CharField(max_length=25,default="user")  # admin or user
    createdby   =  models.IntegerField(default=99) 
    delete1 =    models.IntegerField(default=0)
    STATUS_CHOICES = ( ('', '-SELECT ONE-'),('1', 'ACTIVE'),('0', 'IN-ACTIVE'),('2', 'PROCESS'),    )
    status   = models.TextField(default=1, choices=STATUS_CHOICES) 
    
    class Meta:
        db_table="user_master"
class CurrencyExchange(models.Model):
    from_currency = models.TextField(max_length=10,null=True,default='INR')
    to_currency = models.TextField(max_length=10,null=True,default='INR')
    from_val = models.FloatField(null=True,default=1)
    to_val = models.FloatField(null=True,default=1)
    delete1 = models.IntegerField(null=True,default=0)

    class Meta:
        managed = False
        db_table = 'currency_exchange'
    
    # def save(self, *args, **kwargs):
    #     if self.pk:  # If the object is already saved in the database
    #         orig = CurrencyExchange.objects.get(pk=self.pk)
    #         if orig.from_currency != self.from_currency or orig.to_currency != self.to_currency:
    #             raise ValueError("Cannot change from_currency or to_currency once set.")
    #     super().save(*args, **kwargs)
            

    
    
    
    
