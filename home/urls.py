
from django.urls import path
from .views import StudentAPI, get_book, RegisterView
from .views import StudentAPI, get_book, RegisterView


urlpatterns = [
    path('student/', StudentAPI.as_view(), name='student_list'),  # GET, POST
    path('student/<int:id>/', StudentAPI.as_view(), name='student_detail'),  # PUT, PATCH, DELETE
    path('get-book/', get_book, name='get_book'),
    path('register/', RegisterView.as_view(), name='register'),
]
