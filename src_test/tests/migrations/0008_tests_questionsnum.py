# Generated by Django 4.1.4 on 2023-01-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_tests_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='questionsNum',
            field=models.IntegerField(default=0),
        ),
    ]