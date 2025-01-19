from django.db import models

# Create your models here.


class Budget(models.Model):
    time_period = models.CharField(max_length=50)  # For "Day", "Week", "Year"
    money_used = models.DecimalField(max_digits=10, decimal_places=2)
    account_names = models.TextField()  # Store all account names as a comma-separated string

    def __str__(self):
        return f"{self.time_period} - {self.money_used}"
    class Meta:
        db_table = "Budget"
    
class income(models.Model):
    amasaha=  models.CharField(max_length=255)
    money = models.CharField(max_length=255)
    account= models.CharField(max_length=255)  # Store all account names as a comma-separated string
    impavu=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.amasaha} - {self.money}" 
    class Meta:
        db_table = "income"
class outcome(models.Model):
    amasaha =  models.CharField(max_length=255) 
    money = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    impavu=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.amasaha} - {self.money}"   
    class Meta:
        db_table = "outcome"
class accounts(models.Model):
    account_name = models.CharField(max_length=255)  
    money_save =models.CharField(max_length=255)
    money_out=models.CharField(max_length=255)
    money_total=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.account_name} - {self.money_total}"
    
    class Meta:
        db_table = 'accounts'
        
    