from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
# Create your models here.
class Meal(models.Model):
    #use uuid 4 
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='meals_images',blank=True,null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def no_of_ratings(self):
        ratings_count = Rating.objects.filter(meal=self).count()
        return ratings_count
    def avrage_rating(self):
        sum = 0
        ratings = Rating.objects.filter(meal=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
    def __str__(self):
        return self.name
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    stars = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} rated {self.meal.name} {self.stars} stars'
    class Meta:
        unique_together = [['user', 'meal']]
    