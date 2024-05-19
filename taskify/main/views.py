from django.shortcuts import render,get_object_or_404,redirect
from .models import Tasks,User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

# In views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register_user(request):
    form = forms.UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        print(form.errors)
    return render(request, 'signup.html', {'form': form,'login':False})



from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import login,logout 
def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                User.objects.get(username=username)
            except:
                print('user Doesnt exist')
            user = authenticate(request,username = username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                print('password is wrong')
    context = {'login':True}
    return render(request,'signup.html',context=context)
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
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