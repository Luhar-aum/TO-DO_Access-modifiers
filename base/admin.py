from django.contrib import admin

# Register your models here.
# aum   , password 

from . models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete']
    filter_horizontal = ('allowed_groups',)  # This makes the multi-select UI nicer


admin.site.register(Task,TaskAdmin)