from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ToDo
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
def index(request):
    todo_items = ToDo.objects.all().order_by('-added_date')
    return render(request, 'index.html', {'todo_items':todo_items})

@csrf_exempt
def add_data(request):
    content = request.POST['task']
    current_time = timezone.now()
    ToDo.objects.create(todo_text=content, added_date=current_time)    
    return HttpResponseRedirect('/')

@csrf_exempt
def delete_data(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
