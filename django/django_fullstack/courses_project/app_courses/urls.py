from django.urls import path
from.import views
urlpatterns = [
    path('',views.show_course),
    path('courses/destroy/<int:id>', views.course_specificone),
    path('no',views.no),
    path('yes/<int:id>',views.delete)


]