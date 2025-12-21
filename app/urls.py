from django.urls import path
from .views import HomePageView,CreateTaskView,DeleteTaskView,UpdateTaskView,TaskCompleteView
app_name = 'todo'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('create/',CreateTaskView.as_view(),name='create'),
    path('delete/<int:pk>',DeleteTaskView.as_view(),name='delete'),
    path('update/<int:pk>',UpdateTaskView.as_view(),name='update'),
    path("status/<int:pk>/", TaskCompleteView.as_view(), name="status"),
]

