from django.urls import path
from.import views
urlpatterns = [
    path('registration',views.registration_form),
    path('wall',views.welcome),
    path('login',views.login),
    path('logout',views.logout),
    path('addpost',views.addpost),
    path('delete',views.delete),
    path('addcomment', views.addcomment)
    
]
