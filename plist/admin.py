from django.contrib import admin 
from . models import Image

# Register your models here.
class ImageInline(admin.StackedInline):
    model = Image
    extra = 10

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImageInline]