from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'age', 'nickname']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        # Step 1: Check if 'age' field is in data
        if 'age' in data:
            if data['age'] < 18:
                raise serializers.ValidationError({'error': "Age must be greater than or equal to 18"})

        # Step 2: Check if 'name' field is in data
        if 'name' in data:
            for char in data['name']:
                if char.isdigit():
                    raise serializers.ValidationError({'error': "Name must not contain digits"})

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
