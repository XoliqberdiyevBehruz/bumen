# Generated by Django 4.2 on 2024-09-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='category/logo/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Sub-category',
                'verbose_name_plural': 'Sub-categories',
            },
        ),
    ]
