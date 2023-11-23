from django.urls import path
from.import views
urlpatterns = [
    
    # PATHS FOR BOOKS PAGE
    path('', views.handel_form),
    path('addbooks',views.add_book),
    path('books/<int:id>', views.specific_book),
    path('addauthor_to_book/<int:id2>', views.addauthor_to_book),
    
    # PATHS FOR AUTHORS PAGE
    path('authors',views.handel_authorform),
    path('addauthors',views.add_author),
    path('authors/<int:id3>', views.specific_author),
    path('addbook_to_author/<int:id4>', views.addbook_to_author),
]
