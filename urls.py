from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('testimonials/', views.testimonials, name='blog-testimonials'),
    path('references/', views.references, name='blog-references'),
    path('home_spanish/', views.home_spanish, name='blog-home_spanish'),
    path('testimonials_spanish/', views.testimonials_spanish, name='blog-testimonials_spanish'),
    path('references_spanish/', views.references_spanish, name='blog-references_spanish'),
]
