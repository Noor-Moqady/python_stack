# Generated by Django 2.2.4 on 2023-12-01 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_favorite_books', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='liked_by',
            new_name='users_who_like',
        ),
    ]
