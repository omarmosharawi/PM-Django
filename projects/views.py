from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = 'projects/list.html'
    paginate_by = 3

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('Project_List')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'projects/update.html'
    # success_url = reverse_lazy('Project_List')

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.id])


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Project
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('Project_List')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])


class TaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])