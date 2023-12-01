from django.urls import path
from.import views
urlpatterns = [
    path('',views.registration_form),
    path('books',views.welcome),
    path('login',views.login),
    path('logout',views.logout),
    path('addfavoritebooks', views.addfavoritebooks),
    path('addfav/<int:id>', views.addfav),
    path('books/<int:id>', views.update_specific_book),
    path('removefav/<int:id>', views.removefav),
    path('delete/<int:id>', views.delete)
]
