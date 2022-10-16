from django.db import models

# Create your models here.
class Client(models.Model):
    Invoice_ID = models.CharField(max_length=200, null=False,primary_key = True)
    Branch = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Customer_type = models.CharField(max_length=50)
    Gender = models.CharField(max_length=15)
    Product_line = models.CharField(max_length=50)
    Unit_price = models.FloatField()
    Quantity = models.IntegerField()
    Tax = models.FloatField()
    Total = models.FloatField()
    OrderDate = models.DateField()
    Time = models.TimeField()
    Payment = models.CharField(max_length=20)
    cogs = models.FloatField()
    gross_margin_percentage = models.FloatField()
    gross_income = models.FloatField()
    Rating = models.FloatField()

    class Meta:
        db_table = 'task1'
