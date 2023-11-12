from django.urls import path
from.import views

urlpatterns = [

    path('form', views.display_form),
    path('handel', views.handel_form),
    path('show_result', views.show)
   
]