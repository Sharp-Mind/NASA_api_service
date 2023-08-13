from django.db import models

class Name(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100000)
