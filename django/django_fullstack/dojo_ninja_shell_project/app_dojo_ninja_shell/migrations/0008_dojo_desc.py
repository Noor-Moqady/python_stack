# Generated by Django 2.2.4 on 2023-11-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dojo_ninja_shell', '0007_remove_dojo_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
        ),
    ]
