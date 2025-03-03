from django.urls import path
from .views import api_home,create_task,get_one_task,get_task,delete_task,update_task
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to Task Management API"})

urlpatterns =[
    path('',api_home,name='api_home'),
    path('tasks/',get_task,name='get_task'), 
    path('tasks/create/',create_task,name='create_task'), 
    path('tasks/<int:id>/',get_one_task,name='get_one_task'), 
    path('tasks/update/<int:id>/',update_task,name='update_task'),
    path('tasks/delete/<int:id>/',delete_task,name='elete_task'),

]