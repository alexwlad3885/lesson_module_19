# Generated by Django 5.1.2 on 2024-11-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Сайт')),
                ('publication_date', models.DateTimeField(auto_now=True, verbose_name='Дата опубликования')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={},
        ),
    ]
