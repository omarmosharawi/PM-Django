from django.contrib import admin
from django.db.models import Count
from . import models

# Register your models here.

admin.site.register(models.Category)


# admin.site.register(models.Project)
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'user', 'created_at', 'tasks_count']
    list_per_page = 7
    list_editable = ['status', 'category', 'user']
    list_select_related = ['category', 'user']

    def tasks_count(self, obj):
        # return obj.task_set.count()
        return obj.tasks_count

    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(tasks_count=Count('task'))
        return query


# admin.site.register(models.Task)
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_editable = ['is_completed']
    list_per_page = 7