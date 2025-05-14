
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Student
from .serializers import StudentSerializer


# User Registration (Single or Multiple)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Register new student(s)",
        request_body=StudentSerializer(many=True),
        responses={
            200: "Student(s) created successfully",
            400: "Invalid data"
        }
    )
    def post(self, request):
        is_many = isinstance(request.data, list)
        serializer = StudentSerializer(data=request.data, many=is_many)

        if not serializer.is_valid():
            return Response({
                'status': 400,
                'errors': serializer.errors,
                'message': 'Invalid data'
            })

        serializer.save()
        return Response({
            'status': 200,
            'payload': serializer.data,
            'message': 'Student(s) created successfully'
        })


# Student API with CRUD, Pagination, and Search
class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        manual_parameters=[
            openapi.Parameter(
                'search', openapi.IN_QUERY,
                description="Search students by name",
                type=openapi.TYPE_STRING
            ),
        ],
        responses={200: StudentSerializer(many=True), 404: "Student not found"}
    )
    def get(self, request, id=None):
        if id:
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response({'status': 200, 'payload': serializer.data, 'message': 'Student found successfully'})
            except Student.DoesNotExist:
                return Response({'status': 404, 'message': 'Student not found'})

        search = request.GET.get('search')
        student_objs = Student.objects.all()
        if search:
            student_objs = student_objs.filter(name__icontains=search)

        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(student_objs, request)
        serializer = StudentSerializer(result_page, many=True)

        return paginator.get_paginated_response({
            'status': 200,
            'payload': serializer.data,
            'message': 'Paginated data fetched successfully'
        })

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        request_body=StudentSerializer,
        responses={200: "Student(s) created successfully", 400: "Invalid data"}
    )
    def post(self, request):
        is_many = isinstance(request.data, list)
        serializer = StudentSerializer(data=request.data, many=is_many)

        if not serializer.is_valid():
            return Response({
                'status': 400,
                'errors': serializer.errors,
                'message': 'Invalid data'
            })

        serializer.save()
        return Response({
            'status': 200,
            'payload': serializer.data,
            'message': 'Student(s) created successfully'
        })

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        request_body=StudentSerializer,
        responses={200: "Student updated successfully", 403: "Invalid data", 404: "Student not found"}
    )
    def put(self, request, id):
        try:
            student_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(student_obj, data=request.data)

            if not serializer.is_valid():
                return Response({
                    'status': 403,
                    'errors': serializer.errors,
                    'message': 'Invalid data, please check the fields'
                })

            serializer.save()
            return Response({
                'status': 200,
                'payload': serializer.data,
                'message': 'Student updated successfully'
            })
        except Student.DoesNotExist:
            return Response({'status': 404, 'message': 'Student not found'})

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        request_body=StudentSerializer,
        responses={200: "Student partially updated", 403: "Invalid data", 404: "Student not found"}
    )
    def patch(self, request, id):
        try:
            student_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'status': 403,
                    'errors': serializer.errors,
                    'message': 'Invalid data, please check the fields'
                })

            serializer.save()
            return Response({
                'status': 200,
                'payload': serializer.data,
                'message': 'Student partially updated'
            })
        except Student.DoesNotExist:
            return Response({'status': 404, 'message': 'Student not found'})

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        responses={200: "Student deleted successfully", 404: "Student not found"}
    )
    def delete(self, request, id):
        try:
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status': 200, 'message': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return Response({'status': 404, 'message': 'Student not found'})


# Protected Endpoint Example
class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="A sample protected endpoint",
        responses={200: "Protected endpoint accessed successfully"}
    )
    def get(self, request):
        return Response({"message": "This is a protected endpoint"})


# Simple JSON response endpoint
def get_book(request):
    return JsonResponse({"message": "Yeh get_book ka response hai"})
