from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    message = models.TextField(max_length=256, verbose_name='Сообщение')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __str__(self):
        return f'Заявка от {self.date}'

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
        ordering = ['-date']

