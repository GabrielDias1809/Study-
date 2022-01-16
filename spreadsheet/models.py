from email.policy import default
from random import choice, choices
from socket import SocketIO
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Subjects(models.Model):

    class type_subjects(models.TextChoices):

        Mat1     = 'Arit', _('Aritmética')
        Mat2     = 'Alg', _('Álgebra')
        Mat3     = 'Geom', _('Geometria')
        Port     = 'Port', _('Português')
        Hist     = 'Hist', _('História')
        Geo      = 'Geo', _('Geografia')
        Fis      = 'Fis', _('Física')
        Qui      = 'Qui', _('Química')
        Red      = 'Red', _('Redação')
        Lit      = 'Lit', _('Literatura')
        Socio    = 'Socio',_('Sociologia')
        Filo    = 'Filo',_('Filosofia')

    subjects_in_course      = models.CharField(max_length=7,choices=type_subjects.choices,default=type_subjects.choices)
    verbose_name            = 'Subject'

    def __str__(self):
        return self.subjects_in_course

class Days(models.Model):

    class type_days(models.TextChoices):
            monday      = 'mon', _('Monday')
            tuesday     = 'tues', _('Tuesday')
            wednesday   = 'wed', _('Wednesday')
            thursday    = 'thur', _('Thursday')
            friday      = 'fri', _('Friday')
            saturday    = 'sat', _('Saturday')
            sunday      = 'sun', _('Sunday')


    choose_days             = models.CharField(max_length=10,choices=type_days.choices,default=type_days.monday)
    subjects                = models.ManyToManyField(Subjects)

    def __str__(self):
        return self.choose_days



class Spreadsheet(models.Model):

    days                = models.ManyToManyField(Days)
    course              = models.CharField(max_length=20, help_text="Curso dos seus sonhos!")

    def __str__(self):
        return self.course
    

    

