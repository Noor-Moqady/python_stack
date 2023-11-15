from django.urls import path
from.import views

urlpatterns = [
    
    path('', views.start),
    path('guess', views.guess),
    path('reset', views.reset),
    path('win_show', views.handel),
    path('show', views.show)

   
]