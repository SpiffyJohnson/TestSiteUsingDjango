from django.shortcuts import render
from .models import Student
from .converter import StudentSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Get view
@api_view(['GET'])
def getStudent(request, cNumber):
	try:
		student = Student.objects.get(cNumber = cNumber)
		converter = StudentSerializer(student)
		return Response(converter.data)
	except:
		return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getStudents(request):
	student = Student.objects.all()
	converter = StudentSerializer(student, many=True)
	return Response(converter.data)

@api_view(['POST'])
def createStudent(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getModifyDelete(request, cNumber):
	try:
		student = Student.objects.get(cNumber = cNumber)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		converter = StudentSerializer(student)
		return Response(converter.data)

	elif request.method == 'PUT':
		serializer = StudentSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		student.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)