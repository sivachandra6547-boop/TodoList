from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks=Task.objects.filter( is_created=False).order_by('-updated_at')
 
    completed_tasks=Task.objects.filter(is_created=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }

    return render(request,'home.html',context) 

