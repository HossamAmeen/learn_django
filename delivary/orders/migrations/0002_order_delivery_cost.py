# Generated by Django 4.1.6 on 2023-03-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
