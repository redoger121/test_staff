# Generated by Django 4.1.3 on 2022-11-14 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0002_tests_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tests',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название теста'),
        ),
    ]
