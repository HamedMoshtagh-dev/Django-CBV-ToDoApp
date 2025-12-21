from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task

# صفحه اصلی - فقط تسک‌های کاربر فعلی
class HomePageView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# ایجاد تسک جدید
class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["task"]
    template_name = "index.html"
    success_url = reverse_lazy("todo:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# حذف تسک - فقط توسط صاحب آن
class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home")

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return redirect('todo:home')

# ویرایش تسک - فقط توسط صاحب آن
class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['task']
    template_name = "update.html"
    success_url = reverse_lazy("todo:home")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# تغییر وضعیت انجام شده / انجام نشده - فقط توسط صاحب آن
class TaskCompleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.status = not task.status
        task.save()
        return redirect('todo:home')
