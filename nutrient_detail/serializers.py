from rest_framework import serializers
from .models import nutrient_list


class nutritionserializer(serializers.ModelSerializer):
    class Meta:
        model = nutrient_list
        fields = ['id', 'food_name', 'quantity', 'protien', 'carbohydrate',
                  'fiber', 'sugar', 'saturated_fat', 'polyunsaturated_fat', 'monounsaturated_fat',
                  'trans_fat', 'cholestrol', 'sodium', 'potassium', 'calcium', 'vitaminA', 'vitaminC', 'iron']
