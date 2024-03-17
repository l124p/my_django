# Generated by Django 5.0.3 on 2024-03-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_course_client_kind_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientproduct',
            old_name='kind',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='client',
            name='kind_product',
        ),
        migrations.AddField(
            model_name='client',
            name='products',
            field=models.ManyToManyField(through='shop.ClientProduct', to='shop.kindproduct'),
        ),
        migrations.AddField(
            model_name='clientproduct',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=25),
        ),
        migrations.AlterUniqueTogether(
            name='kindproduct',
            unique_together={('product', 'kind')},
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name',)},
        ),
    ]
