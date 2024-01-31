from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('register/', views.register, name='register'),
    path('single/', views.single, name='single'),
    path('typo/', views.typo, name='typo'),
]