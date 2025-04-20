from django.urls import path
from . import views

urlpatterns = [
    # FBV
    path('courses/', views.course_list, name='course-list'),
    path('enroll/', views.enroll_course, name='enroll-course'),
    path('categories/', views.category_list, name='category-list'),

    # CBV
    path('courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    path('enrollments/', views.EnrollmentListView.as_view(), name='user-enrollments'),
]
