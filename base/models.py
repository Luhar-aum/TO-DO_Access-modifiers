from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.

class Task(models.Model):
    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('protected', 'Protected'),
    ]
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')

    allowed_groups = models.ManyToManyField(Group, blank=True)
    # allowed_users = models.ManyToManyField(User, related_name='allowed_tasks', blank=True)  # For protected tasks
    #  groups that can access protected tasks



    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']





# for protected

# from django import forms
# from django.contrib.auth.models import Group

# class TaskForm(forms.ModelForm):
#     allowed_groups = forms.ModelMultipleChoiceField(
#         queryset=Group.objects.all(),
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         label="Allowed Groups (for protected tasks only)"
#     )

#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'complete','allowed_groups']
#         widgets = {
#             'allowed_groups': forms.CheckboxSelectMultiple(),
#         }

    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.instance.visibility = 'protected'   #default it is set as protected
