from django.db import models

# Create your models here.
class Property (models.Model):
    property_name = models.CharField(max_length=200)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    description = models.CharField()
    price = models.DecimalField(max_digits=10)
    contact = models.CharField(max_length=13)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.property_name
class Category (models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
class Location (models.Model):
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.location_name

class Image (models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
