from django.contrib import admin
from .models import *
from .models import Book

admin.site.register(Student)  # ✅ Correct
admin.site.register(Category)  # ✅ 
admin.site.register(Book)  # ✅
