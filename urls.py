from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('testimonials/', views.testimonials, name='blog-testimonials'),
    path('services/', views.services, name='blog-services'),
    path('references/', views.references, name='blog-references'),
    path('home_spanish/', views.home_spanish, name='blog-home_spanish'),
]
