from .models import Meal, Rating
from django.contrib.auth.models import User
from rest_framework import serializers
class MealSerialier(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','name','description','image','created_at','updated_at','no_of_ratings','avrage_rating']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only':True,'required':True}}