# Generated by Django 4.1.3 on 2022-12-02 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_office', '0012_alter_url_url_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='img_href',
            field=models.URLField(blank=True),
        ),
    ]
