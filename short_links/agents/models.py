from django.db import models
from managers.models import Manager


class Agent(models.Model):
    name = models.CharField(max_length=75, verbose_name="Имя агента")
    surname = models.CharField(max_length=75, verbose_name="Фамилия агента")
    link_agent = models.CharField(max_length=195, verbose_name="Ссылка", blank=True)
    agent_phone = models.CharField(max_length=12, verbose_name="Номер телефона Агента", unique = True)
    manager_personal = models.ForeignKey(Manager, on_delete=models.PROTECT)
    inviteAgent = models.IntegerField(verbose_name="Кто пригласил",null=True)
    lenInvited = models.IntegerField(verbose_name="Количество приглашений",default=0)

    class Meta:
        verbose_name = 'Агента'
        verbose_name_plural = 'Агенты'

    def __str__(self):
        return f"{self.name}{self.surname}"


