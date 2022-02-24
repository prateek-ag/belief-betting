# Generated by Django 4.0.2 on 2022-02-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='system_direction',
            field=models.CharField(choices=[(1, 'Buy'), (0, 'Sell')], max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='system_price',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
    ]