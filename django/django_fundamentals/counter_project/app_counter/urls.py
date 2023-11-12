from django.urls import path
from.import views

urlpatterns = [
    
    path('visits', views.counter),
    path('addcount',views.counter2),
    path('reset',views.reset),
    path('delete',views.delete)
]