from django.shortcuts import render
from .models import Meal,Rating
from .serializers import MealSerialier, RatingSerializer,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import (TokenAuthentication,
                                           BaseAuthentication,
                                         
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
class MealViewSet(viewsets.ModelViewSet):
    '''
    here we define the viewset for the Meal model

    '''

    
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    queryset = Meal.objects.all()
    serializer_class = MealSerialier
    @action(detail=True,methods=['POST'])
    def rate_meal(self,request,pk=None):
        
        if not request.user.is_authenticated:
            return Response({'message': 'You must be authenticated to rate meals'}, 
                          status=status.HTTP_401_UNAUTHORIZED)
        meal = Meal.objects.get(id=pk)
        user = request.user
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


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user = user)
            response = {
                "user":serializer.data,
                "token":token.key
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

"""login view"""
class LoginView(APIView):

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username,password = password)
        if user:
            token,created = Token.objects.get_or_create(user=user)
            response = {
                "token":token.key
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response({'error':'invalid information'},status=status.HTTP_400_BAD_REQUEST)

