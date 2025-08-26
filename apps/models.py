from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField, IntegerField, PositiveIntegerField
from django_ckeditor_5.fields import CKEditor5Field


class Category(Model):
    title = CharField(max_length=100)
    icon = CharField(max_length=10)


class Product(Model):
    title = CharField(max_length=100)
    price = IntegerField()
    # rating =
    count = PositiveIntegerField()
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    description = CKEditor5Field()


class ProductImage(Model):
    image = ImageField()
    product = ForeignKey('apps.Product', CASCADE, related_name='images')
