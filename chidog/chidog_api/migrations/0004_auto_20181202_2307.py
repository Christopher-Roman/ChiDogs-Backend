# Generated by Django 2.1.3 on 2018-12-02 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chidog_api', '0003_auto_20181201_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='post_pic',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='posted_pic',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='upload_pic',
        ),
    ]