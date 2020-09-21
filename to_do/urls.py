from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('to_do/', views.add_data, name='to%do'),
    path('delete_todo/<int:todo_id>', views.delete_data)
]