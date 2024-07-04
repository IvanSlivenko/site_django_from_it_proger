from django.db import models

class Task(models.Model):
    title = models.CharField(verbose_name='Назва', max_length=50)
    task = models.TextField(verbose_name='Завдання', max_length=500)
    date_task = models.DateField(verbose_name='Дата завдання')
    date_result = models.DateField(verbose_name='Дата виконання')
    status = models.CharField(verbose_name='Статус', max_length=9)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'
