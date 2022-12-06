from django.db import models

# Create your models here.


class nutrient_list(models.Model):

    food_name = models.CharField(max_length=50)
    quantity = models.FloatField()
    protien = models.FloatField()
    carbohydrate = models.FloatField()
    fiber = models.FloatField()
    sugar = models.FloatField()
    saturated_fat = models.FloatField()
    polyunsaturated_fat = models.FloatField()
    monounsaturated_fat = models.FloatField()
    trans_fat = models.FloatField()
    cholestrol = models.FloatField()
    sodium = models.FloatField()
    potassium = models.FloatField()
    calcium = models.FloatField()
    vitaminA = models.FloatField()
    vitaminC = models.FloatField()
    iron = models.FloatField()


def __str__(self):
    return self.food_name
