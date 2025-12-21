from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Task
from django.urls import reverse_lazy
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.


class HomePageView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    
    
class CreateTaskView(CreateView):
    model = Task
    fields = ["task"]
    template_name = "index.html"
    success_url = reverse_lazy("todo:home")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home")
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('todo:home')
    
    
class UpdateTaskView(UpdateView):
    model = Task
    fields = ['task']
    success_url = reverse_lazy("todo:home")
    template_name = "update.html"


class TaskCompleteView(View):
    model = Task
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.status = not task.status  # تغییر وضعیت
        task.save()
        return redirect('todo:home')