# Generated by Django 2.2.4 on 2023-11-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dojo_ninja_shell', '0004_remove_dojo_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='old dojo', max_length=225),
        ),
    ]
