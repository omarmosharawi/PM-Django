from django import forms
from . import models


attributes = {'class': 'form-control'}


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs=attributes),
            'description': forms.Textarea(attrs=attributes),
            'category': forms.Select(attrs=attributes),
        }
        
        
class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['status', 'description', 'category']
        widgets = {
            'status': forms.Select(attrs=attributes),
            'description': forms.Textarea(attrs=attributes),
            'category': forms.Select(attrs=attributes),
        }