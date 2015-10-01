#! coding: utf-8
from _ast import mod
from django.db import models
from django.contrib.auth.models import User

statuses = ('To Do', 'In Progress', 'Testing', 'Done', 'Сanceled')
TASKS_STATUSES = zip(xrange(len(statuses)), statuses)

class projects(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __unicode__(self):
        return self.name

class tasks(models.Model):
    title = models.CharField('Название', max_length=150)
    projects = models.ForeignKey(projects, verbose_name='Проект')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(User, verbose_name='Ответственный', blank=True, null=True)
    statuses = models.IntegerField('Статус', choices=TASKS_STATUSES, default=0)

    class Meta:
        ordering = ['title']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __unicode__(self):
        return self.title

class comments(models.Model):
    task = models.ForeignKey(tasks, verbose_name='Задача')
    user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True)
    comment = models.TextField('Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __unicode__(self):
        return self.task.title

class tasks_files(models.Model):
    task = models.ForeignKey(tasks, verbose_name='Задача')
    file = models.FileField('Файл')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __unicode__(self):
        return self.task.title

class positions(models.Model):
    name = models.CharField('Наименование', max_length=150)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __unicode__(self):
        return self.name

class users_param(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    position = models.ForeignKey(positions, verbose_name='Должность')

    class Meta:
        verbose_name = 'Настройки пользователей'
        verbose_name_plural = 'Настройки пользователей'

    def __unicode__(self):
        return str(self.user)


