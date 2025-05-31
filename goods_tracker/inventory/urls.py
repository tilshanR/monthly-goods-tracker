from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-item/', views.home, name='add_item'),
    path('monthly/', views.monthly_list, name='monthly_list'),
]
