from django.urls import path,include
from .views import RatingViewSet, MealViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('meals', MealViewSet, basename='meal')
router.register('ratings', RatingViewSet, basename='rating')
urlpatterns = [
path('api-auth/', include('rest_framework.urls')),
path('', include(router.urls)),
path('api-token-auth/', obtain_auth_token )

]
