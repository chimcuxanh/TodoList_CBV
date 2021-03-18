from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
# cai nay la yeu cau dang nhap moi dc vao
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'toto/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'toto/task.html'


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('home')
    context_object_name = 'edit'
    template_name = 'toto/edit.html'


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('home')
    context_object_name = 'update'
    template_name = 'toto/update.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('home')
    context_object_name = 'delete'
    template_name = 'toto/delete.html'