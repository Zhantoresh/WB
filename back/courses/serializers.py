from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Category, Course, Enrollment

# 1. Serializer (не ModelSerializer) — для User создания вручную
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

# 2. ModelSerializer для профиля
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio']

# 3. ModelSerializer для категорий
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# 4. ModelSerializer для курсов
class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'instructor', 'description', 'price', 'is_active', 'category', 'category_id']

# 5. Serializer (не ModelSerializer) для записи на курс (Enrollment), можно кастомизировать
class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)  # Для отображения вложенного курса
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'course_id', 'enroll_date', 'status']
