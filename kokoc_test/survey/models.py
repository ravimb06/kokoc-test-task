from django.db import models
 
class QuestionModel(models.Model):
    """Модель вопроса с вариантами ответа."""
    question = models.TextField(null=True, verbose_name='Вопрос')
    option_1 = models.CharField(null=True, verbose_name='Вариант ответа 1')
    option_2 = models.CharField(null=True, verbose_name='Вариант ответа 2')
    option_3 = models.CharField(null=True, verbose_name='Вариант ответа 3')
    option_4 = models.CharField(null=True, verbose_name='Вариант ответа 4')
    answer = models.CharField(null=True, verbose_name='Правильный ответ')
    
    def __str__(self):
        return self.question
