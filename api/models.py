from django.db import models


# Create your models here.
# Создание модели базы даннных

# python manage.py migrate

class Organization(models.Model):
    """ таблица с организациями """
    name_organization = models.CharField(max_length=150, verbose_name='Название')


class Author(models.Model):
    """ таблица с авторами """
    name_author = models.CharField(max_length=150, verbose_name='Автор')
    salary = models.IntegerField()
    position = models.CharField(max_length=150, verbose_name='Должность')
    year = models.IntegerField()
    award_name = models.CharField(max_length=150, verbose_name='Награды')
    # organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return (f'<Author> id: {self.id}, Name:{self.name_author}, Salary: {self.salary}, Position: {self.position}, '
                f'Year: {self.year}, Award: {self.award_name}')
