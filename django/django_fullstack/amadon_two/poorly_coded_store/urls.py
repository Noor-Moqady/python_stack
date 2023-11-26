from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete', views.delete),
    path('checkout/<int:id>', views.checkout)
]