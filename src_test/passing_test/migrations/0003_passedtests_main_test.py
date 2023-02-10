# Generated by Django 4.1.4 on 2023-01-25 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0012_alter_testquestions_name'),
        ('passing_test', '0002_passedanswers_real_answer_passedtests_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passedtests',
            name='main_test',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='tests.tests'),
        ),
    ]
