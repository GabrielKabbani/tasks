from django.shortcuts import render
from django.http.response import JsonResponse as resp
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from tasks.serializers import TaskSerializer
from tasks.models import Task

#functions:

def delete_all():
    Task.objects.all().delete()
    return resp({'Done': 'Ordered items were deleted'})

def post(request):
    task_data = JSONParser().parse(request)
    task_serializer = TaskSerializer(data=task_data)
    if task_serializer.is_valid():
        task_serializer.save()
        return resp(task_serializer.data) 
    else:
        return resp({'Worked': 'Did not work'})

def get(request):
    getee = request.GET.get('title', None)
    serial = TaskSerializer(Task.objects.all(), many=True)
    if getee:
        tasks = Task.objects.all().filter(title__icontains=getee)
    serial = TaskSerializer(Task.objects.all(), many=True)
    return resp(serial.data)



# Create your views here.
@api_view(["GET", "POST", "DELETE"])
def execute(request):
    if request.method == 'DELETE':
        return delete_all()
    elif request.method == 'POST':
        return post(request)
    elif request.method == 'GET':
        return get(request)
        

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
