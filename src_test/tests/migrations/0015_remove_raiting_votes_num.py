# Generated by Django 4.1.4 on 2023-01-30 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0014_remove_tests_raiting_alter_themeoftests_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raiting',
            name='votes_num',
        ),
    ]
