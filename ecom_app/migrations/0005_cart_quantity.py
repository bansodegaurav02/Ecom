# Generated by Django 4.0.6 on 2024-02-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0004_remove_cart_quantity_alter_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]