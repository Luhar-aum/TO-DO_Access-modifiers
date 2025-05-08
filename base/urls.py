from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,CustomLoginView,RegisterPage 
from .views import dashboard,delete_task,add_public_task,add_protected_task
from django.contrib.auth.views import LogoutView

urlpatterns=[


        
        path('/dashboard', dashboard, name='dashboard'),
        path('delete-task/<int:task_id>/',delete_task, name='delete_task'),
        path('add-public-task/', add_public_task, name='add_public_task'),
        path('add_protected_task/', add_protected_task, name='add_protected_task'),


        path('login/',CustomLoginView.as_view(),name='login'),
        path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
        path('register/',RegisterPage.as_view(),name='register'),
        path('',TaskList.as_view(),name='tasks'),
        path('task/<int:pk>',TaskDetail.as_view(),name='task'),
        path('task-create/',TaskCreate.as_view(),name='task-create'),
        path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
        path('task-delete/<int:pk>',DeleteView.as_view(),name='task-delete')

]