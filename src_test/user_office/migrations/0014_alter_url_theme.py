# Generated by Django 4.1.4 on 2023-01-30 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0014_remove_tests_raiting_alter_themeoftests_image_and_more'),
        ('user_office', '0013_vacancy_img_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.themeoftests', unique=True),
        ),
    ]
