from django import forms
from . import models


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'category': forms.Select(),
        }
        
        
class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['status', 'description', 'category']
        widgets = {
            'status': forms.Select(),
            'description': forms.Textarea(),
            'category': forms.Select(),
        }