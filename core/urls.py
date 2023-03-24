from django.urls import path
from . import views


# url patterns
urlpatterns = [
    path('', views.courses, name='courses'),
    path('modules/', views.modules, name='modules'),
    path('tutors/', views.tutors, name='tutors'),
]
