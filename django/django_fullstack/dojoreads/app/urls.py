from django.urls import path
from.import views
urlpatterns = [
    path('',views.registration_form),
    path('books',views.welcome),
    path('login',views.login),
    path('logout',views.logout),
    path('books/add',views.addbook_review),
    path('books/<int:id>',views.showbook),
    path('addreview/<int:id>', views.addreview),
    path('delete/<int:id>/<int:id2>',views.delete),
    path('users/<int:id>', views.specific_user)
    
]
