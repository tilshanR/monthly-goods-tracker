from django.contrib import admin
from .models import Item, MonthlyEntry, MonthlyGood

# Register your models here.
admin.site.register(Item)
admin.site.register(MonthlyEntry)
admin.site.register(MonthlyGood)
