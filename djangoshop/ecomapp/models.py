from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit



class Category(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        #slug = slugify(translit(unicode_literals(instance.name), reversed=True))
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
