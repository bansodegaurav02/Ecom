# Generated by Django 4.0.6 on 2024-02-18 13:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom_app', '0011_all'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='all',
            new_name='all_1',
        ),
    ]
