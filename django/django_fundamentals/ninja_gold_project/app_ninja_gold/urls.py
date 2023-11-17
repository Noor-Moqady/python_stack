from django.urls import path
from . import views

urlpatterns = [
    path('', views.ninja_gold_page),
    path('process_money', views.process_money),
    path('reset', views.reset),
    path('<str:location>', views.process_money)

   
]