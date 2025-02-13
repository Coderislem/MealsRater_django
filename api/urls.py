from django.urls import path,include
from .views import RatingViewSet, MealViewSet,UserViewSet,LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('meals', MealViewSet, basename='meal')
router.register('ratings', RatingViewSet, basename='rating')
router.register('users',UserViewSet,basename='user')


urlpatterns = [
path('api-auth/', include('rest_framework.urls')),
path('', include(router.urls)),
# login 
path('login/',LoginView.as_view(),name='login'),

path('api-token-auth/', obtain_auth_token ),


]
