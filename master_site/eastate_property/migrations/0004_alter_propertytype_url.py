# Generated by Django 4.0.1 on 2022-01-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eastate_property', '0003_propertytype_alter_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertytype',
            name='url',
            field=models.SlugField(default='Дом', max_length=130, unique=True),
        ),
    ]
