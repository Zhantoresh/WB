# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .models import Course, Enrollment, Category
from .serializers import CourseSerializer, EnrollmentSerializer, CategorySerializer

# === Function-Based Views (FBV) ===

@api_view(['GET'])
def course_list(request):
    courses = Course.objects.filter(is_active=True)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_course(request):
    course_id = request.data.get('course')  # обязательно 'course', не 'course_id'
    if Enrollment.objects.filter(user=request.user, course_id=course_id).exists():
        return Response({'detail': 'Already enrolled'}, status=status.HTTP_400_BAD_REQUEST)

    data = request.data.copy()
    data['user'] = request.user.id

    serializer = EnrollmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# === Class-Based Views (CBV) ===

class CourseCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollmentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        enrollments = Enrollment.objects.filter(user=request.user)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)
