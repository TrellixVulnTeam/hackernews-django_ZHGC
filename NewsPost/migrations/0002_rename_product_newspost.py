# Generated by Django 4.0.5 on 2022-06-12 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPost', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='NewsPost',
        ),
    ]
