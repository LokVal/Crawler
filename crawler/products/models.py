import uuid
from datetime import timedelta, datetime
from django.db import models


def get_id_field():
    return models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class BaseModel(models.Model):

    class Meta:
        app_label = 'products'


class Manufacturer(models.Model):
    id = get_id_field()
    create_date = models.DateTimeField()
    mod_date = models.DateTimeField(null=True)

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        app_label = 'products'



class ProductBrand(models.Model):
    id = get_id_field()
    create_date = models.DateTimeField()
    mod_date = models.DateTimeField(null=True)

    name = models.CharField(max_length=50, unique=True)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'products'


class Product(models.Model):
    id = get_id_field()
    create_date = models.DateTimeField(default=datetime.now)
    mod_date = models.DateTimeField(null=True)

    asin = models.CharField(max_length=20, null=True)
    model_number = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=1024, unique=True)
    product_title = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    bsr = models.FloatField(null=True)
    customer_rating = models.IntegerField(null=True)
    rating_amount = models.IntegerField(null=True)
    product_brand_id = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True)
    published = models.DateTimeField(null=True)
    dim_x = models.FloatField(null=True)
    dim_y = models.FloatField(null=True)
    dim_z = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    shipping_weight = models.FloatField(null=True)

    class Meta:
        app_label = 'products'


class ProductAudit(models.Model):
    id = get_id_field()
    create_date = models.DateTimeField()
    mod_date = models.DateTimeField(null=True)

    property_name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    old_value = models.TextField()
    new_value = models.TextField()

    class Meta:
        app_label = 'products'


class CrawlingTask(models.Model):
    id = get_id_field()
    create_date = models.DateTimeField()
    mod_date = models.DateTimeField(null=True)

    asin = models.CharField(max_length=20, null=True)
    url = models.CharField(max_length=256, null=True)
    interval = models.DurationField(default=int(timedelta(days=1).total_seconds()), null=False)

    class Meta:
        app_label = 'products'


class TaskRun(models.Model):
    id = get_id_field()
    create_date = models.DateTimeField()
    mod_date = models.DateTimeField(null=True)

    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    class Meta:
        app_label = 'products'
