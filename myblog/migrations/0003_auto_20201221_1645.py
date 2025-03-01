# Generated by Django 3.1.4 on 2020-12-21 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_blogpost_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title_tag',
            field=models.CharField(max_length=100),
        ),
    ]
