from django.db import models
from django.utils.timezone import now

# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    date = models.DateField()
    file_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tree(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name

class Person(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.DO_NOTHING, related_name='members')
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    sources = models.ManyToManyField(Source, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='events')
    type = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f'{self.type}: {self.date}'