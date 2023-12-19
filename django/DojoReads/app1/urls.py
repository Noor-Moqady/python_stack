from django.urls import path
from . import views
urlpatterns = [
    path('',views.main ),
    path('registration', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('books/add', views.addbook),
    path('books/add_procces', views.addbook_procces),
    path('books/<int:id>', views.book_added),
    path('review/add_procces', views.addreview_procces),
    path('users/<int:id>', views.user),
    path('delete/<int:id>', views.delete_book),
    path('delete/review/<int:id>', views.delete_review),




]