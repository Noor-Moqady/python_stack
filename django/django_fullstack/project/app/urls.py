from django.urls import path
from.import views
urlpatterns = [
    path('',views.registration_form),
    path('books',views.welcome),
    path('login',views.login),
    path('logout',views.logout),
    path('addbook',views.addbook),
    path('addtofavorite/<int:id>',views.addtofavorite) ,
    path('books/<int:id>', views.specific_book_update)  ,
    path('remove/<int:id>', views.remove),
    path('delete/<int:id>', views.delete)
]
