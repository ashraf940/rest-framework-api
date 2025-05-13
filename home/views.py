from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from .models import Student
from .serializers import StudentSerializer

#  User Registration (Single or Multiple)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        is_many = isinstance(request.data, list)
        serializers = StudentSerializer(data=request.data, many=is_many)

        if not serializers.is_valid():
            return Response({
                'status': 400,
                'errors': serializers.errors,
                'message': 'Invalid data'
            })

        serializers.save()

        return Response({
            'status': 200,
            'payload': serializers.data,
            'message': 'Student(s) created successfully'
        })


# Student API with CRUD + Pagination + Search
class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    #  GET with Search + Pagination
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

    #  POST (Single or Multiple Students)
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

    #  PUT (Full Update)
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

    #  PATCH (Partial Update)
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

    #  DELETE by ID
    def delete(self, request, id):
        try:
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({
                'status': 200,
                'message': 'Student deleted successfully'
            })
        except Student.DoesNotExist:
            return Response({'status': 404, 'message': 'Student not found'})
