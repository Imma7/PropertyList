from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Property (models.Model):
    property_name = models.CharField(max_length=200)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    contact = models.CharField(max_length=13)
    type_of_listing = models.ForeignKey('ListingType', on_delete=models.CASCADE, null=True)
    type_of_property = models.ForeignKey('PropertyType', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Meta orders posts by created at in ascending order and verbose name plural name Property as Properties in the admin page
    class Meta: 
        ordering = ['-created_at'] 
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.property_name
class ListingType (models.Model):
    listing_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Listing Types"

    def __str__(self):
        return self.listing_name

class PropertyType (models.Model):
    asset_type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Property Types"
    
    def __str__(self):
        return self.asset_type
class Location (models.Model):
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.location_name

class Image (models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    # Uploads with dates saves the images in folder uploads and their respective dates
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    
    def __str__(self):
        return '%s - %s' % (self.property, self.image)
