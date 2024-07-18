from django.db import models


class Todo(models.Model):
    title = models.CharField('Что нужно сделать', max_length=400)
    is_complete = models.BooleanField('Фух закончил', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title


