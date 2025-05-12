# from django.urls import path
# from .views import home, post_student  # Make sure post_student is defined in views.py

# urlpatterns = [
#     path('', home, name='home'),
#     path('post_student/', post_student, name='post_student'),
# ]
from django.contrib import admin
from django.urls import path ,include
from .views import StudentAPI, get_book, RegisterView

from .views import *

urlpatterns = [
    path('student/' ,StudentAPI.as_view()),




    # path('', home, name='home'), 
    # path('student/', home, name='home'),  
    # path('post_student/', post_student, name='post_student'),
    # path('update_student/<int:id>/', update_student, name='update_student'),
    # path('delete_student/<int:id>/', delete_student, name='delete_student'),
    path('get-book/', get_book),
    path('register/', RegisterView.as_view())

 ]