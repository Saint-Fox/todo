from django.urls import path
from .views import main_view, update_task, delete_task

urlpatterns = [
    path('', main_view, name='main-view'),
    path('update_task/<str:pk>', update_task, name='update-task'),
    path('delete_task/<str:pk>', delete_task, name='delete-task'),
]