# Generated by Django 3.0.5 on 2020-04-21 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_parser', '0003_productpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
    ]
