# Generated by Django 4.0.2 on 2022-02-22 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='system_price',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
    ]