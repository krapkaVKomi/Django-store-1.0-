# Generated by Django 4.1 on 2022-10-04 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_rename_photo_news_%y-%m-%d-%h-%m-%s'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='%Y-%m-%d-%H-%M-%S',
            new_name='test',
        ),
    ]
