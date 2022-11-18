from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} {self.lastName}"

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Site(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    favicon = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.description}"

class SectionRenderer(models.Model):
        
    name = models.CharField(max_length=100)
    templatePath = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.templatePath}"

class Section(models.Model):

    name = models.CharField(max_length=100)
    site = models.ForeignKey(Site,on_delete=models.CASCADE)
    renderer = models.ForeignKey(SectionRenderer,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.renderer}"

class ComponentRenderer(models.Model):
        
    name = models.CharField(max_length=100)
    templatePath = models.CharField(max_length=200)
    specifics= models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} - {self.templatePath}"

class Component(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    renderer = models.ForeignKey(ComponentRenderer,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.Renderer}"


class Guest(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    places = models.IntegerField()
    confirmed = models.CharField(max_length=1)
    #def __init__(self,id,confirmed):
    #    self.id = id
    #    self.confirmed=confirmed

    def __str__(self):
        return f"{self.name}"




