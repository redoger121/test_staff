# Generated by Django 4.1.3 on 2022-11-11 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeOfTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тема теста')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название теста')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('theme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.themeoftests', verbose_name='тема теста')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='TestQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='текст вопроса')),
                ('for_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.tests', verbose_name='Вопрос для теста')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ответ')),
                ('answer_is_true', models.BooleanField(default=False, verbose_name='Верный ответ')),
                ('for_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.testquestions')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
