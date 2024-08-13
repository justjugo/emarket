from django.urls import path
from .views import get_all_product,get_by__id_product

urlpatterns =[
    path('product/',get_all_product,name= 'get_all_product'),
     path('product/<str:pk>',get_by__id_product,name= 'get_by__id_product'),
]