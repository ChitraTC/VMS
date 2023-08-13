# from django.urls import reverse_lazy
# from django.contrib.auth import login
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Task
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.

# class based
class CustomLoginView(LoginView):
    template_name = 'login1.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return  super(RegisterView,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return  redirect('task_list')
        return super(RegisterView, self).get(*args,**kwargs)


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasklist.html'

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['task']=context['task'].filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields = ['title','description','completed']
    success_url=reverse_lazy('task_create') #redirect to task)create html
    template_name = 'taskcreate.html'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('task_list')
    template_name = 'taskcreate.html'

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
    template_name = 'taskdelete.html'

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    fields = ['user','title', 'description','created', 'completed']
    template_name = 'taskdetail.html'

def send_text_email(request):
    subject = "Hi welcome to django maiing session"
    message = "This is test email sent from django"
    from_email = 'pdjangotest@gmail.com'
    recepient_list = ['chitratchandran@gmail.com']
    send_mail(subject,message,from_email,recepient_list)
    return HttpResponse('Test email sent successfully...!')