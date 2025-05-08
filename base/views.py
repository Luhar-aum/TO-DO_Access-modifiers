from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy    
from .models import Task

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin    #roles :- user can be admin,user 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import models
from django.contrib.auth.models import Group


# @login_required
def dashboard(request):
    # Public tasks: visible to everyone
    public_tasks = Task.objects.filter(visibility='public')
    
    # Private tasks: visible only to the owner
    private_tasks = Task.objects.filter(user=request.user, visibility='private') if request.user.is_authenticated else []
    
    # Protected tasks: visible to the owner and any allowed users
    protected_tasks = Task.objects.filter(
        Q(visibility='protected') & (Q(user=request.user) | Q(allowed_groups__in=request.user.groups.all()))
    ).distinct() if request.user.is_authenticated else []
    
    return render(request, 'base/dashboard.html', {
        'public_tasks': public_tasks,
        'private_tasks': private_tasks,
        'protected_tasks': protected_tasks,
    })




from django.shortcuts import get_object_or_404

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('dashboard')




def add_public_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Task.objects.create(
                title=title,
                description=description,
                visibility='public'
            )
        return redirect('dashboard')  # Redirect back to the dashboard after adding a task
    return render(request, 'base/add_public_task.html')



@login_required
def add_protected_task(request):
    if request.method == 'POST':
        form = models.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            if task.visibility == 'protected':
                task.save()
                form.save_m2m()  # Save the allowed groups
            else:
                task.save()
            return redirect('dashboard')
    else:
        form = models.TaskForm()
    return render(request, 'base/add_protected_task.html', {'form': form})



#this is for the protected task here

# def create_task(request):
#     form = models.TaskForm(request.POST or None)
#     if form.is_valid():
#         task = form.save(commit=False)
#         task.user = request.user
#         task.save()
#         form.save_m2m()  # Save allowed_groups


#             # Add a group programmatically
#         group = Group.objects.get(name='Managers')
#         task.allowed_groups.add(group)

#         return redirect('task_list')
#     else:
#         form.TaskForm()
#     return render(request, 'tasks/create.html', {'form': form})













class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user =  True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'    
    form_class = UserCreationForm
    redirect_authenticated_user =  True   #not working
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)    
        return super(RegisterPage,self).form_valid(form)
    

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage,self).get(*args,**kwargs)


class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name= 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        # for searching purpose
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']= context['tasks'].filter(title__startswith=search_input)   #title__icontains used for getting all realed words in the list
            tasks= tasks.filter(title_startswith=search_input)

        context['search_input'] = search_input
        return context



class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task   
    context_object_name = 'task'      # object IS BY DEFAULT 



class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    # fields = '__all__'
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    # fields = '__all__'
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin,DeleteView):
    model =Task
    context_object_name='task'
    success_url = reverse_lazy('tasks')
