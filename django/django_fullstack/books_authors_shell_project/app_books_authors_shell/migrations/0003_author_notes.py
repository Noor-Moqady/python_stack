# Generated by Django 2.2.4 on 2023-11-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_books_authors_shell', '0002_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(default='nooooootes', max_length=45),
        ),
    ]
