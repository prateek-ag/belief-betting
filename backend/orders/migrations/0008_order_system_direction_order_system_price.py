# Generated by Django 4.0.2 on 2022-02-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_order_system_direction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='system_direction',
            field=models.CharField(choices=[(1, 'Buy'), (0, 'Sell')], default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='system_price',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]
