# Generated by Django 5.0.3 on 2024-03-22 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0012_product_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='start_date',
        ),
    ]
