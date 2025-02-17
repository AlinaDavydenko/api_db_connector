from django.db import models

# Create your models here.

# python manage.py migrate


class TestAuthor(models.Model):
    """ таблица с авторами """
    id_author = models.IntegerField()
    name_authors = models.CharField(max_length=150, verbose_name='Автор')
    salary = models.IntegerField()
    position = models.CharField(max_length=150, verbose_name='Должность')
    year = models.IntegerField()
    award_name = models.CharField(max_length=150, verbose_name='Награды')

    class Meta:
        db_table = 'hh_testauthor'  # Укажите имя вашего приложения

    def __str__(self):
        return f'''
        <Author> id: {self.id}, Name:{self.name_authors}, Salary: {self.salary}, Position: {self.position}, 
        Year: {self.year}, Award: {self.award_name}
'''
