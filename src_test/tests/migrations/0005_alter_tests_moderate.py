# Generated by Django 4.1.3 on 2022-11-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_tests_moderate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='moderate',
            field=models.CharField(choices=[('OM', 'На проверке'), ('NM', 'Не проверено'), ('MO', 'Проверено'), ('RE', 'Отказано в публикации')], default='NM', max_length=20, verbose_name='статус'),
        ),
    ]
