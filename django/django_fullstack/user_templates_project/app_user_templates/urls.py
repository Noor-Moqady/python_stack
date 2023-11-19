from django.urls import path
from.import views
urlpatterns = [
    path('', views.method1),
    path('handel', views.method2),
    path('allusers',views.method3)
]
