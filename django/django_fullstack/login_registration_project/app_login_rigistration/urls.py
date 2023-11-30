from django.urls import path
from.import views
urlpatterns = [
    path('',views.registration_form),
    path('success',views.welcome),
    path('login',views.login),
    path('logout',views.logout)
    
]
