# Generated by Django 3.1.4 on 2020-12-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_categories_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='slug',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='categories',
            field=models.CharField(max_length=100),
        ),
    ]
