from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=255)

class MonthlyEntry(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    month=models.DateField()