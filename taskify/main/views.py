from django.shortcuts import render,get_object_or_404,redirect
from .models import Tasks,User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    incompletedTask = Tasks.objects.filter(user=user,completeStatus=False).order_by('priority')
    completedTask = Tasks.objects.filter(user=user,completeStatus=True).order_by('priority')
    
    context = {'user':user,
               'incompletedTask':incompletedTask,
               'completedTask':completedTask,
               } 
    
    if request.method == 'GET' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        item_id = request.GET.get('item_id')
        item = Tasks.objects.get(id=item_id)
        context['task'] = item
    if request.method == 'POST':
        item_id = request.POST.get('task_id')
        task_ = Tasks.objects.get(id=item_id)
        task_.completeStatus = True
        task_.save()
    return render(request,'dashboard.html',context)

def taskDetail(request,task_id):
    task = get_object_or_404(Tasks,id=task_id)
    data = {
        'id':task.id,
        'title':task.Title,
        'description':task.Description,
        'dueDate':task.dueDate,
        'priority':task.dueDate,
        'completeStatus':task.completeStatus
    }

    return JsonResponse(data)



from . import forms
def newTask(request):
    form = forms.newTask()
    if request.method == 'POST':
        newtask = forms.newTask(request.POST)
        if newtask.is_valid():
            instance = newtask.save(commit=False)
            instance.user_id = request.user.id
            instance.save()
            return redirect('dashboard')
    return render(request,'newtask.html',context={'form':form})

def updateTask(request,task_id):
    print(request)
    task = get_object_or_404(Tasks,id=task_id)
    task.completeStatus = True
    task.save()
    return JsonResponse({'success':True})


def delTask(request,task_id):
    task = get_object_or_404(Tasks,id=task_id)
    task.delete()
    return JsonResponse({'success':True})

def editTask(request):
    taskId = request.GET.get('pk')
    task = get_object_or_404(Tasks,id=taskId)
    if request.method == 'POST':
        form = forms.newTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form =  forms.newTask(instance=task)
    return render(request,'newtask.html',context={'form':form})