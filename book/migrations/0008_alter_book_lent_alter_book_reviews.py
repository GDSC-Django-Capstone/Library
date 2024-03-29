# Generated by Django 5.0.3 on 2024-03-15 14:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_book_total_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='lent',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='book',
            name='reviews',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=3000), blank=True, default=list, size=None),
        ),
    ]
