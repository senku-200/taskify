from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),
    path('admin',admin.site.urls,name='admin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('task/<int:task_id>/',views.taskDetail),
    path('update/<int:task_id>/',views.updateTask),
    path('newTask',views.newTask,name='newtask'),
    path('deltask/<int:task_id>/',views.delTask),
    path('edittask/',views.editTask,name='edittask'),
    path('registeruser/',views.register_user,name='RegisterUser'),
    path('login/',views.user_login,name='login'),
    path('logout/', views.logout, name='logout'),
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)