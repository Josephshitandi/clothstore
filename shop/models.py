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

class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name='cate')
    image2 = CloudinaryField('image_2', blank=True, null=True)

    def __str__(self):
        return self.name

    def save_sub_category(self):
        self.save()

    def delete_sub_category(self):
        self.delete()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(_('date of order'), auto_now_add=True)
    product_id = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name='order')
    delivered = models.BooleanField()

    # def __str__(self):
    #     return self.date

    def save_order(self):
        self.save()

    def delete_order(self):
        self.delete()