# Generated by Django 4.2.2 on 2023-07-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='number_of_views',
            field=models.IntegerField(default=0, verbose_name='просмотры'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='содержание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='sign_of_publication',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
    ]
