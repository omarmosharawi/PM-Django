from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = 'projects/list.html'
    paginate_by = 3

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('Project_List')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'projects/update.html'
    # success_url = reverse_lazy('Project_List')

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.id])

    def test_func(self):
        return self.get_object().user_id == self.request.user.id


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Project
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('Project_List')

    def test_func(self):
        return self.get_object().user_id == self.request.user.id


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin,  CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def test_func(self):
        project_id = self.request.POST.get('project', '')
        return models.Project.objects.get(pk=project_id).user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Task

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])