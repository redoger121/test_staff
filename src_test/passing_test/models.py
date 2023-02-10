from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from tests.models import *
# class PassedTests(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     tested_at=models.DateTimeField(verbose_name='Даиы и время тестирования', auto_now_add=True)
#     test=models.ForeignKey(Tests, on_delete=models.PROTECT)
#     questions=models.ManyToManyField(TestQuestions)
#     answers=models.ManyToManyField(Answers)



class PassedTests(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name='Название теста', unique=False)
    theme_id = models.ForeignKey(ThemeOfTests, on_delete=models.CASCADE, verbose_name='тема теста')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    score=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    test_id=models.PositiveIntegerField(default=0)
    test_closed=models.BooleanField(default=False)
    main_test=models.ForeignKey(Tests, on_delete=models.CASCADE, blank=True, default=1)
    rait=models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name


class PassedTestQuestions(models.Model):
    name = models.CharField(max_length=200, verbose_name='текст вопроса')
    for_test=models.ForeignKey(PassedTests, verbose_name='Вопрос для теста', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.name





class PassedAnswers(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ответ')
    real_answer=models.BooleanField(default=False)
    answer_is_true = models.BooleanField(default=False, verbose_name='Верный ответ')
    for_question = models.ForeignKey(PassedTestQuestions, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.name




