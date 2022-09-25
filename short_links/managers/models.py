from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=75, verbose_name="Имя менеджера")
    surname = models.CharField(max_length=75, verbose_name="Фамилия менеджера")
    idFromBitrix = models.IntegerField(verbose_name="ID в битриксе",unique=True)
    agents =  models.IntegerField(verbose_name="Количество агентов",default=0)

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        return f"{self.name} {self.surname}"
