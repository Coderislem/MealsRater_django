from .models import Meal, Rating
from rest_framework import serializers
class MealSerialier(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','name','description','image','created_at','updated_at','no_of_ratings','avrage_rating']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
