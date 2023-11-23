from django.urls import path
from.import views
urlpatterns = [
    path('shows/new',views.shows_form),
    path('shows', views.shows_table),
    path('delete/<int:id>', views.delete),
    path('shows/<int:id>', views.shows_specificone),
    path('shows/<int:id>/edit', views.shows_update)
]
