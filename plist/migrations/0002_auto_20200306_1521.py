# Generated by Django 3.0.3 on 2020-03-06 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Properties'},
        ),
    ]
