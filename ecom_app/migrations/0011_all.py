# Generated by Django 4.0.6 on 2024-02-18 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom_app', '0010_delete_duo'),
    ]

    operations = [
        migrations.CreateModel(
            name='all',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_app.product_rating')),
            ],
        ),
    ]
