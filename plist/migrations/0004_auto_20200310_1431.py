# Generated by Django 3.0.3 on 2020-03-10 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plist', '0003_auto_20200310_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listingtype',
            old_name='listing_type',
            new_name='listing_name',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='listings',
            new_name='type_of_listing',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='properties',
            new_name='type_of_property',
        ),
        migrations.RenameField(
            model_name='propertytype',
            old_name='property_type',
            new_name='asset_type',
        ),
    ]
