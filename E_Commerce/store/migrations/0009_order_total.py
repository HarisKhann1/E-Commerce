# Generated by Django 5.1.4 on 2025-01-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order_product_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
