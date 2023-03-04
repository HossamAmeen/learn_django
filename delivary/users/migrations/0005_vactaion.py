# Generated by Django 4.1.6 on 2023-03-04 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_admin_options_alter_callcenter_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vactaion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.TextField(null=True)),
                ('note', models.TextField(null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accept', 'Accept'), ('cancel', 'Cancel')], default='pending', max_length=20)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vaction', related_query_name='vacations', to='users.delivery')),
            ],
        ),
    ]
