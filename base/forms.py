from django import forms
from django.contrib.auth.models import Group
from .models import Task


class TaskForm(forms.ModelForm):
    allowed_groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Allowed Groups (for protected tasks only)"
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete','allowed_groups']
        widgets = {
            'allowed_groups': forms.CheckboxSelectMultiple(),
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.visibility = 'protected'   #default it is set as protected
