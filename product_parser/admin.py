from django.contrib import admin
from .models import Manufacturer, ProductBrand, Product, CrawlingTask, ProductPage

admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(Manufacturer)
admin.site.register(CrawlingTask)
admin.site.register(ProductPage)
