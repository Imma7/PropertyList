from django.contrib import admin 
from . models import Image, Property, Category, Location

# Register your models here.
class ImageInline(admin.StackedInline):
    model = Image
    extra = 10

class PropertyAdmin(admin.ModelAdmin):
    # Model Admin field Options
    list_display = ('property_name', 'description', 'location', 'price', 'category', 'created_at')
    list_filter = ('property_name', 'location', 'price', 'category')
    search_fields = ('property_name',)
    inlines = [ImageInline]
    

admin.site.register(Image)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Location)
admin.site.register(Category)