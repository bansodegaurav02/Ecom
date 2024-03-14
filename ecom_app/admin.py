from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(products)
admin.site.register(category)
admin.site.register(cart)
admin.site.register(product_rating)
admin.site.register(orders_data)

