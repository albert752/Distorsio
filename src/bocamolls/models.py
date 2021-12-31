from django.db import models
from django.utils import timezone


class Professor(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='nom')
    last_name = models.CharField(max_length=200, verbose_name='cognoms')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom')
    acronym = models.CharField(max_length=200, verbose_name='sigles')


class Bocamoll(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='professor')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, verbose_name='subject')
    text = models.TextField(verbose_name='text')
    date = models.DateField(default=timezone.now, verbose_name='data')
    aproved = models.FloatField(default=False, verbose_name='estat')
