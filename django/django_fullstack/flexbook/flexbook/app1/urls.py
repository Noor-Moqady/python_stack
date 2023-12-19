from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_registration),
    path('FLEXBOOK', views.main),
    path('registration', views.registre_proccess),
    path('login', views.login_proccess),
    path('post', views.post),
    path('comment/<int:id>', views.comment),
    path('change_avatar', views.change),
    path('update_avatar', views.update),
    path('like/<int:id>', views.like),
    path('control', views.control),
    path('control/<int:id>', views.control_del),
    path('add/<int:id>', views.add_friend),
    path('delete/<int:id>', views.delete_post),
    path('delete_comment/<int:id>', views.delete_comment),
    path('logout', views.logout),
]
