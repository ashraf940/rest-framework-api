# # # from django.urls import path
# # # from .views import home, post_student  # Make sure post_student is defined in views.py

# # # urlpatterns = [
# # #     path('', home, name='home'),
# # #     path('post_student/', post_student, name='post_student'),
# # # ]
# # from django.contrib import admin
# # from django.urls import path ,include
# # from .views import StudentAPI, get_book, RegisterView

# # from .views import *

# # urlpatterns = [
# #     path('student/' ,StudentAPI.as_view()),

    
# #     path('student/', StudentAPI.as_view(), name='student_list'),  # For GET and POST
# #     path('student/<int:id>/', StudentAPI.as_view(), name='student_detail'),  # For PUT, PATCH, DELETE


# #     path('student/', StudentAPI.as_view(), name='student_list'),

# #     # For GET, PUT, PATCH, DELETE requests for a specific student by ID
# #     path('student/<int:id>/', StudentAPI.as_view(), name='student_detail'),



# #     # path('', home, name='home'), 
# #     # path('student/', home, name='home'),  
# #     # path('post_student/', post_student, name='post_student'),
# #     # path('update_student/<int:id>/', update_student, name='update_student'),
# #     # path('delete_student/<int:id>/', delete_student, name='delete_student'),
# #     path('get-book/', get_book),
# #     path('register/', RegisterView.as_view())

# #  ]


# from django.urls import path
# from .views import StudentAPI, get_book, RegisterView

# urlpatterns = [
#     path('student/', StudentAPI.as_view(), name='student_list'),  # For GET and POST
#     path('student/<int:id>/', StudentAPI.as_view(), name='student_detail'),  # For PUT, PATCH, DELETE
#     path('get-book/', get_book),
#     path('register/', RegisterView.as_view())
# ]


from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('student/', StudentAPI.as_view()),                  # GET (list), POST
    path('student/<int:id>/', StudentAPI.as_view()),         # PUT, PATCH (detail)
]
