# Generated by Django 4.0.1 on 2022-01-20 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='quote_autor',
            field=models.CharField(blank=True, max_length=60, verbose_name='Автор цитаты'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text_quote',
            field=models.TextField(blank=True, verbose_name='Цитата'),
        ),
    ]
