# Generated by Django 5.0.3 on 2024-03-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='./book/static/book'),
        ),
    ]
