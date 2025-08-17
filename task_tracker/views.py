from django.shortcuts import render
from task_tracker import models
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import TaskForm

# Create your views here.

class TaskListView(ListView):
    model = models.Task
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = models.Task
    success_url = reverse_lazy('task-list')
    form_class = TaskForm
  
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
