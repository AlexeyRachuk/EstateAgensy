# Generated by Django 4.0.1 on 2022-01-20 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate_blog', '0013_rename_url_category_url_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url_cat',
        ),
    ]
