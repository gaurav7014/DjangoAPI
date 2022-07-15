from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('carts' , CarttView.as_view() ),
    # path('carts/<int:pk>/', CartDetail.as_view()),
    path('carts/<int:pk>/', UserCartDetail.as_view()),

    # path('demo' , DemoView.as_view()),
]