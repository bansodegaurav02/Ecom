# Generated by Django 4.0.6 on 2024-02-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0016_remove_orders_data_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_data',
            name='status',
            field=models.CharField(choices=[('APPROVED', 'APPROVED'), ('DELIVERD', 'DELIVERD')], default='pending', max_length=100),
        ),
    ]
