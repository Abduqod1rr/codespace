from django.shortcuts import render , redirect 
from .forms import CustomUsercreationForm
from .models import CustomUser
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout 


class RegisterView(CreateView):
    model = CustomUser
    form_class=CustomUsercreationForm
    template_name='register.html'
    success_url=reverse_lazy('login')


class login(LoginView):
    template_name= 'login.html'
    fields=['username','password']
    success_url=reverse_lazy('home')
    
    
def logoutuser(request):
    logout(request)
    return redirect(reverse_lazy('login'))
   