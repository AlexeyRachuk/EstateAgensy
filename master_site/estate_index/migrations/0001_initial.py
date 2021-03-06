# Generated by Django 4.0.1 on 2022-02-14 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estate_agents', '0002_agent_property_agent'),
        ('eastate_property', '0014_alter_propertygallery_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название компании')),
                ('descr', models.TextField(max_length=500, verbose_name='Описание в подвале')),
                ('phone', models.CharField(help_text='Номер без +7', max_length=10, verbose_name='Номер телефона в подвале')),
                ('email', models.EmailField(max_length=254, verbose_name='Email в подвале')),
                ('copywrite', models.CharField(max_length=100, verbose_name='Копирайт в подвале')),
                ('index_agents', models.ManyToManyField(related_name='agent_index', to='estate_agents.Agent', verbose_name='Лушие агенты')),
            ],
            options={
                'verbose_name': 'Главная',
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название сайта')),
                ('url', models.CharField(max_length=100, verbose_name='Ccылка на сайт')),
            ],
            options={
                'verbose_name': 'Сайты в подвале',
                'verbose_name_plural': 'Сайты в подвале',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя отзыва')),
                ('descr', models.TextField(max_length=500, verbose_name='Отзыв')),
                ('photo', models.ImageField(null=True, upload_to='review/', verbose_name='Фото отзыва')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_id', to='estate_index.index')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='index',
            name='sites',
            field=models.ManyToManyField(related_name='sites_list', to='estate_index.Sites', verbose_name='Сайты в подвале'),
        ),
        migrations.AddField(
            model_name='index',
            name='slider',
            field=models.ManyToManyField(related_name='property_index', to='eastate_property.Property', verbose_name='Обеъекты слайдера'),
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название преимущества')),
                ('descr', models.CharField(max_length=500, verbose_name='Описание преимущества')),
                ('benefits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits_id', to='estate_index.index')),
            ],
            options={
                'verbose_name': 'Преимущества',
                'verbose_name_plural': 'Преимущества',
            },
        ),
    ]
