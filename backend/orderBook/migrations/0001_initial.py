# Generated by Django 3.2.14 on 2022-08-01 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted', models.DateTimeField(auto_now=True)),
                ('fill_type', models.CharField(choices=[('M', 'Market'), ('P', 'Price')], max_length=20)),
                ('price', models.DecimalField(decimal_places=4, max_digits=6)),
                ('direction', models.CharField(choices=[('B', 'Buy'), ('S', 'Sell')], max_length=2)),
                ('quantity', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.AddConstraint(
            model_name='orderbook',
            constraint=models.UniqueConstraint(fields=('order_id',), name='unique order_id'),
        ),
    ]