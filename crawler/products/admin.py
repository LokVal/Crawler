from django.contrib import admin

# Register your models here.
from crawler.products.models import Manufacturer, ProductBrand, Product

admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(Manufacturer)