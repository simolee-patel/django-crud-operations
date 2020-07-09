from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import task
from .forms import taskForm


def index(request):
    tasks= task.objects.all()
    form =  taskForm()
    if(request.method == 'POST'):
        form= taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'tasks':tasks, 'form':form}
    return render(request, 'templates/list.html' , context)

def updateTask(request , pk):
    tasks= task.objects.get(id= pk)
    form = taskForm(instance=tasks)
    if (request.method =='POST'):
        form = taskForm(request.POST ,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request ,'templates/update.html', context)

def deleteTask(request , pk):
    tasks= task.objects.get(id= pk)
    if (request.method=='POST'):
        tasks.delete()
        return redirect('/')
    context={'tasks':tasks}
    return render(request , 'templates/delete.html', context )