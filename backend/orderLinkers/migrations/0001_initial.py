# Generated by Django 3.2.14 on 2022-08-01 14:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLinker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fill_quantity', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(1, message='Must fill at least one unit!')])),
                ('fill_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('datetime_filled', models.DateTimeField(auto_now=True)),
                ('comission_order_1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('comission_order_2', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linker_order_1', to='orders.order')),
                ('order_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linker_order_2', to='orders.order')),
            ],
        ),
    ]