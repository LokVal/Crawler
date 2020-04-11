import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# def get_id_field():
#     return models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#

# class Manufacturer(models.Model):
#     id = get_id_field()
#     create_date = models.DateTimeField()
#     mod_date = models.DateTimeField(null=True)
#
#     name = models.CharField(max_length=50, unique=True)
#
#
# class ProductBrand(models.Model):
#     id = get_id_field()
#     create_date = models.DateTimeField()
#     mod_date = models.DateTimeField(null=True)
#
#     name = models.CharField(max_length=50, unique=True)
#     manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
#
#
# class Product(models.Model):
#     id = get_id_field()
#     create_date = models.DateTimeField(default=datetime.now)
#     mod_date = models.DateTimeField(null=True)
#
#     asin = models.CharField(max_length=20, null=True)
#     model_number = models.CharField(max_length=50, null=True)
#     url = models.CharField(max_length=1024, unique=True)
#     product_title = models.CharField(max_length=100)
#     price = models.FloatField(null=True)
#     bsr = models.FloatField(null=True)
#     customer_rating = models.IntegerField(null=True)
#     rating_amount = models.IntegerField(null=True)
#     product_brand_id = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True)
#     published = models.DateTimeField(null=True)
#     dim_x = models.FloatField(null=True)
#     dim_y = models.FloatField(null=True)
#     dim_z = models.FloatField(null=True)
#     weight = models.FloatField(null=True)
#     shipping_weight = models.FloatField(null=True)
#
#
# class ProductAudit(models.Model):
#     id = get_id_field()
#     create_date = models.DateTimeField()
#     mod_date = models.DateTimeField(null=True)
#
#     property_name = models.CharField(max_length=30)
#     type = models.CharField(max_length=30)
#     old_value = models.TextField()
#     new_value = models.TextField()
#
#
# class CrawlingTask(models.Model):
#     id = get_id_field()
#     create_date = models.DateTimeField()
#     mod_date = models.DateTimeField(null=True)
#
#     asin = models.CharField(max_length=20, null=True)
#     url = models.CharField(max_length=256, null=True)
#     interval = models.DurationField(default=int(timedelta(days=1).total_seconds()), null=False)
#
#
# class TaskRun(models.Model):
#     id = get_id_field()
#     create_date = models.DateTimeField()
#     mod_date = models.DateTimeField(null=True)
#
#     product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

# import requests
# from dataclasses import dataclass
#
# import schedule
# from bs4 import BeautifulSoup
#
# from crawler.users.models import Product, CrawlingTask
#
#
# @dataclass
# class TableItem:
#     key: str
#     value: str
#
#
# def create_soup(asin, url) -> BeautifulSoup:
#     # ASIN = 'B081CB3RJJ'
#     url = 'https://www.amazon.com/dp/' + asin if asin else url
#
#     # url = 'https://www.amazon.com/CamelBak-Chute-Water-Bottle-Glass/dp/B07663TZNT/ref=sr_1_1?dchild=1&qid=1585992016&s=sporting-goods&sr=1-1'
#     headers = {
#         "User-Agent": 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
#     }
#     resp = requests.get(url) #  , proxies={'socks5': '153.3.7.164:1080'})
#     soup = BeautifulSoup(resp.content, features="lxml")
#
#     if 'Sorry, we just need to make sure you\'re not a robot' in soup.text:
#         raise Exception('The site thinks you are a robot.')
#
#     return soup
#
#
# def run_crawler(asin, url) -> Product:
#     soup_outcome = create_soup(asin, url)
#
#     product_title = soup_outcome.select("#productTitle")[0].get_text().strip()
#     product_price = soup_outcome.select("#priceblock_saleprice")[0].get_text().strip()
#     product_reviews_number = soup_outcome.select("#acrCustomerReviewText")[0].get_text().strip()
#     text_bullets = [
#         b.text.replace('\n', '').replace('\t', '')
#         for b in soup_outcome.select('#feature-bullets > ul > li > span')
#         if len(list(b.children)) < 2
#     ]
#     table_values = [
#         TableItem(
#             t.findChild('th').text.replace('\n', '').replace('  ', ''),
#             t.findChild('td').text.replace('\n', '').replace('  ', '')
#         )
#         for t in soup_outcome.select('.prodDetTable tr')
#     ]
#
#     product = Product(
#         title=product_title,
#         price=product_price,
#         rating_amount=product_reviews_number
#         )
#
#     Product.objects.create(product)
#
#     return product
#
#
# def register_tasks():
#     registered_jobs = []
#     for task in CrawlingTask.objects.all():
#         job = schedule.every(task.interval)\
#             .seconds.do(lambda: run_crawler(task.asin, task.url))
#         registered_jobs.append(job)
#
#     schedule.run_all()
#
#     return registered_jobs
#
#
# def unregister_task(job):
#     schedule.cancel_job(job)

