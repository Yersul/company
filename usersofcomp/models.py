from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class UsersRole(MPTTModel):
    name = models.CharField(max_length=25, verbose_name="Имя")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, verbose_name="Позиция", null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self):
        return self.name


class CompUsers(models.Model):
    name = models.CharField(max_length=25, verbose_name="Имя")
    surname = models.CharField(max_length=25, verbose_name="Фамилия")
    employed = models.DateField(null=False, verbose_name="Дата принятия")
    salary = models.IntegerField(null=False, verbose_name="Зарплата")
    position = models.ForeignKey(UsersRole, on_delete=models.CASCADE, verbose_name="Позиция")

    class Meta:
        verbose_name = "Наш Юзер"
        verbose_name_plural = "Наши Юзеры"

    def __str__(self):
        return self.name


