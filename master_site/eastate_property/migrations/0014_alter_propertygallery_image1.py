# Generated by Django 4.0.1 on 2022-02-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eastate_property', '0013_remove_propertygallery_image_propertygallery_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertygallery',
            name='image1',
            field=models.ImageField(help_text='Певрое фото обязательное, осатльные нет', upload_to='property_photos/', verbose_name='Фото объекта 1'),
        ),
    ]
