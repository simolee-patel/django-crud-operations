from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name="task"),
    path('update/<str:pk>', views.updateTask , name="update_task"),
    path('delete/<str:pk>', views.deleteTask, name="delete_task")
]
