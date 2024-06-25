from django import forms
from . import models


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['title', 'description', 'category']
        wedgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'category': forms.Select(),
        }