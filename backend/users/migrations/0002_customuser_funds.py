# Generated by Django 4.0.2 on 2022-02-23 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='funds',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=99),
        ),
    ]
