from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class surveyModel(models.Model):
    name = models.CharField(max_length = 100)
    war_and_peace = models.IntegerField()
    immigration = models.IntegerField()
    gun_control = models.IntegerField()
    crime = models.IntegerField()
    drugs = models.IntegerField()
    civil_rights = models.IntegerField()
    jobs = models.IntegerField()
    environment = models.IntegerField()
    budget_and_economy = models.IntegerField()
    tax_reform = models.IntegerField()
    social_security = models.IntegerField()
    infrastructure = models.IntegerField()
    education = models.IntegerField()
    healthcare = models.IntegerField()
    abortion = models.IntegerField()

    def __str__(self):
        return f'Name: {self.name}'
