from django.urls import path
from.import views
urlpatterns = [
    path('', views.handel_form),
    path('adddojo', views.add_dojo),
    path('addninja', views.add_ninja),
    path('delete', views.delete)
]
