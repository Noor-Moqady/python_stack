from django.urls import path
from.import views
urlpatterns = [
    path('',views.registration_form),
    path('books',views.welcome),
    path('login',views.login),
    path('logout',views.logout),
    path('addfavoritebooks', views.addfavoritebooks)
    
]
