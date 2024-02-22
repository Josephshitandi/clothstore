from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    image2 = CloudinaryField('image_2', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=100, blank=True, null=True)
    shipped_from = models.ForeignKey("Shop", on_delete=models.CASCADE, related_name='shop')
    size = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    sub_category = models.ForeignKey(
        "Sub_Category", on_delete=models.CASCADE, related_name='sub_categ')

    def __str__(self):
        return self.item_name

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()

class Category(models.Model):
    category = models.CharField(max_length=100)
    image = CloudinaryField('image')
    card = CloudinaryField('card')

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()