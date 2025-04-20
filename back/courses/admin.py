from django.contrib import admin
from .models import UserProfile, Category, Course, Enrollment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'price', 'category', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'instructor']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'enroll_date', 'status']
    list_filter = ['status', 'enroll_date']
    search_fields = ['user__username', 'course__title']
