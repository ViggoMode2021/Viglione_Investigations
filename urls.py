from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('testimonials/', views.testimonials, name='blog-testimonials'),
    path('services/', views.services, name='blog-services'),
    path('references/', views.references, name='blog-references'),
    path('pay_invoice/', views.pay_invoice, name='blog-pay_invoice'),
]
