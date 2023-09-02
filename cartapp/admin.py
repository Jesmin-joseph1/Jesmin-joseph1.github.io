from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cart)

class ItemsAdmin(admin.ModelAdmin):
    list_display = ['products', 'cart', 'quantity', 'active']

admin.site.register(Items, ItemsAdmin)
