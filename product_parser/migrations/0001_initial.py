# Generated by Django 3.0.5 on 2020-04-16 19:17

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlingTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(null=True)),
                ('asin', models.CharField(max_length=20, null=True)),
                ('url', models.CharField(max_length=256, null=True)),
                ('interval', models.DurationField(default=86400)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('mod_date', models.DateTimeField(null=True)),
                ('asin', models.CharField(max_length=20, null=True)),
                ('model_number', models.CharField(max_length=50, null=True)),
                ('url', models.CharField(max_length=1024, unique=True)),
                ('product_title', models.CharField(max_length=100)),
                ('price', models.FloatField(null=True)),
                ('bsr', models.FloatField(null=True)),
                ('customer_rating', models.IntegerField(null=True)),
                ('rating_amount', models.IntegerField(null=True)),
                ('published', models.DateTimeField(null=True)),
                ('dim_x', models.FloatField(null=True)),
                ('dim_y', models.FloatField(null=True)),
                ('dim_z', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('shipping_weight', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAudit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(null=True)),
                ('property_name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('old_value', models.TextField()),
                ('new_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskRun',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(null=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_parser.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('manufacturer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_parser.Manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_brand_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_parser.ProductBrand'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
