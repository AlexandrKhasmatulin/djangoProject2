# Generated by Django 4.2.2 on 2023-07-08 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_number_of_views_alter_blog_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='sign_of_publication',
            new_name='is_published',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='number_of_views',
            new_name='views_count',
        ),
    ]