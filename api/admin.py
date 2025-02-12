from django.contrib import admin
from .models import Meal, Rating

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'created_at')  # عرض هذه الحقول في قائمة الأدمن
    search_fields = ('name', 'description')  # البحث داخل الاسم والوصف
    list_filter = ('created_at', 'updated_at')  # التصفية حسب التاريخ والسعر
    ordering = ('-created_at',)  # ترتيب البيانات تنازليًا حسب تاريخ الإنشاء

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('meal', 'user', 'stars', 'created_at')  # عرض هذه الحقول
    search_fields = ('meal__name', 'user__username')  # البحث حسب اسم الوجبة واسم المستخدم
    list_filter = ('stars', 'created_at')  
    ordering = ('-created_at',)  
