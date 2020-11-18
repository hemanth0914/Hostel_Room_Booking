from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.home, name='home'),
    path('student/sample/', views.sam, name='sample'),
    path('student/floor/<str:pk>/', views.floor, name='floor'),
    path('student/rooms/<str:pk>/', views.rooms, name='rooms'),
    path('student/profile/', views.student, name='student'),
    path('warden/profile', views.warden, name='warden'),
    path('confirmation/booking/<str:pk>/',views.booking_form_views,name='confirmation_booking')
]
