# Generated by Django 4.1.6 on 2023-03-10 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_client_address_2'),
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertracking',
            name='delivery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delivery', to='users.delivery'),
        ),
    ]
