# Generated by Django 4.1.3 on 2022-11-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_office', '0009_remove_url_href_remove_url_site_url_url_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='href',
            field=models.URLField(),
        ),
    ]