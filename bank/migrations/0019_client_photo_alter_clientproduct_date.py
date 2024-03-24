# Generated by Django 5.0.3 on 2024-03-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0018_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/client_photos', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='clientproduct',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата открытия'),
        ),
    ]
