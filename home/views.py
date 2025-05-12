
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token




@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({'status': 200, 'payload': serializer.data})

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


#auth token
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializers = UserSerializer(data=request.data)
        if not serializers.is_valid():
            return Response({'status': 403, 'errors': serializers.errors, 'message': 'Invalid data'})
        user = serializers.save()
        user = User.objects.get(username = serializers.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status': 200, 
                         'payload': serializers.data,
                         'refresh': str(refresh), 
                         'access': str(refresh.access_token),
                         'message': 'User created successfully'})


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication




class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]

#api view

    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        print(request.user)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self,request):
        serializers = StudentSerializer(data=request.data)
        if not serializers.is_valid():
            print(serializers.errors)
            return Response({'status': 400, 'errors': serializers.errors, 'message': 'Invalid data'})
        serializers.save()
        return Response({'status': 200, 'payload': serializers.data, 'message': 'Student created successfully'})
        

    def put(self,request):
        try:
            Student_obj = Student.objects.get(id = request.data['id'])
            serializers = StudentSerializer(Student_obj, data=request.data, partial=False)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({'status': 403, 'errors': serializers.errors, 'message': 'Invalid data'})
            serializers.save()
            return Response({'status': 200, 'payload': serializers.data, 'message': 'Student updated successfully'})
        except Exception as e:
            return Response({'status': 403, 'message': 'Student not found'})

    def patch(self,request):
        try:
            Student_obj = Student.objects.get(id = request.data['id'])
            serializers = StudentSerializer(Student_obj, data=request.data, partial=True)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({'status': 403, 'errors': serializers.errors, 'message': 'Invalid data'})
            serializers.save()
            return Response({'status': 200, 'payload': serializers.data, 'message': 'Student updated successfully'})
        except Exception as e:
            return Response({'status': 403, 'message': 'Student not found'})


    def delete(self,request):
        try:
            id = request.GET.get('id')
            Student_obj = Student.objects.get(id = id)
            Student_obj.delete()
            return Response({'status': 200, 'message': 'Student deleted successfully'})
        except Exception as e:
            return Response({'status': 403, 'message': 'Student not found'})











# @api_view(['GET'])
# def home(request):
#     Student_objs = Student.objects.all()
#     serializer = StudentSerializer(Student_objs, many=True)
#     return Response({'status': 200, 'payload': serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data=data) 
    
#     if serializer.is_valid():
#         serializer.save()  
#         return Response({
#             'status': 200, 'payload': serializer.data, 'message': 'Student created successfully'
#         })
    
#     return Response({
#         'status': 400,'errors': serializer.errors, 'message': 'Invalid data'})

# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)

#         serializer = StudentSerializer(student_obj, data=request.data)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 400, 'errors': serializer.errors, 'message': 'Invalid data'})
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'message': 'Student updated successfully'})
        
#     except Exception as e:
#         return Response({'status': 403, 'message': 'Student not found'})
   

# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status': 200, 'message': 'Student deleted successfully'})
#     except Exception as e:
#         return Response({'status': 403, 'message': 'Student not found'})
    

