# Generated by Django 5.0.3 on 2024-03-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0019_client_photo_alter_clientproduct_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/product_photos', verbose_name='Фото'),
        ),
    ]
