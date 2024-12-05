from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.create_task, name='create_task'),
    path('list/', views.list_task, name='list_task'),
]