# Generated by Django 4.1 on 2022-10-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_alter_news_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/%H/%M/%S', verbose_name='Фото'),
        ),
    ]
