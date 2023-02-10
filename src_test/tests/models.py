from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ThemeOfTests(models.Model):
    name = models.CharField(max_length=35, verbose_name='Тема теста', unique=True)
    image=models.ImageField(blank=True, upload_to='themes_images/', null=True)
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class TestQuestions(models.Model):
    name = models.CharField(max_length=600, verbose_name='')
    for_test=models.ForeignKey('Tests', verbose_name='Вопрос для теста', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.name


class Answers(models.Model):
    name = models.CharField(max_length=600, verbose_name='')
    answer_is_true = models.BooleanField(default=False, verbose_name='Верный ответ')
    for_question = models.ForeignKey(TestQuestions, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.name


class Tests(models.Model):
    NOT_MODERATE = 'NM'
    ON_MODERATING = 'OM'
    MODERATED ='MO'
    REFUSED='RE'

    ORDER_STATUS_CHOICES = (
        (ON_MODERATING, 'На проверке'),
        ( NOT_MODERATE, 'Не проверено'),
        (MODERATED, 'Проверено'),
        (REFUSED, 'Отказано в публикации'),

    )




    creator=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Название теста')
    theme_id = models.ForeignKey(ThemeOfTests, on_delete=models.CASCADE, verbose_name='тема теста')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    moderate=models.CharField(verbose_name='статус', max_length=20, choices=ORDER_STATUS_CHOICES, default=NOT_MODERATE)
    image=models.ImageField(upload_to='tests_images/', blank=True)
    test_rait=models.DecimalField(max_digits=5 ,decimal_places=2, default=0)
    visited=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    questionsNum=models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name

class Raiting(models.Model):
    test=models.ForeignKey(Tests, on_delete=models.CASCADE, verbose_name='Тест')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mark=models.IntegerField(default=0)

