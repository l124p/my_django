# Generated by Django 5.0.3 on 2024-03-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_remove_product_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
