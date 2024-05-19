from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin',admin.site.urls,name='admin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('task/<int:task_id>/',views.taskDetail),
    path('update/<int:task_id>/',views.updateTask),
    path('newTask',views.newTask,name='newtask'),
    path('deltask/<int:task_id>/',views.delTask),
    path('edittask/',views.editTask,name='edittask'),
]
