# Generated by Django 5.0.3 on 2024-03-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_alter_product_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateField(default='2099-12-31', verbose_name='Срок действия'),
        ),
    ]
