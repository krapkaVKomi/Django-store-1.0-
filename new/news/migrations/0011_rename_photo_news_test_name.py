# Generated by Django 4.1 on 2022-10-04 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_rename_test_news_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='photo',
            new_name='test_name',
        ),
    ]