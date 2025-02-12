from django.shortcuts import render
from .models import Meal,Rating
from .serializers import MealSerialier, RatingSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User
# Create your views here.


# class MealListCreate(ListCreateAPIView):
#     queryset = Meal.objects.all()
#     serializer_class = MealSerialier
# class MealRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Meal.objects.all()
#     serializer_class = MealSerialier
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerialier
    @action(detail=True,methods=['POST'])
    def rate_meal(self,request,pk=None):
        meal = Meal.objects.get(id=pk)
        username = request.data.get('username')
        user = User.objects.get(username=username)
        stars = request.data.get('stars')
        try:
            rating = Rating.objects.get(user=user,meal=meal)
            rating.stars = stars
            rating.save()
            serializer = RatingSerializer(rating,many=False)
            response = {'message':'Rating updated','result':serializer.data}
            return Response(response,status=status.HTTP_200_OK)
        except:
            rating = Rating.objects.create(user=user,meal=meal,stars=stars)
            serializer = RatingSerializer(rating,many=False)
            response = {'message':'Rating created','result':serializer.data}
            return Response(response,status=status.HTTP_200_OK)

# class RatingListCreate(ListCreateAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
# class RatingRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer