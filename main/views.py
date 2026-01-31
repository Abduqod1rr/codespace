from django.shortcuts import render
from .models import CodeFile
from django.urls import reverse_lazy
from django.views.generic import CreateView ,DeleteView ,ListView   ,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CodeFileListView(ListView):
    model = CodeFile
    template_name = "home.html"



class CreateFile(LoginRequiredMixin,CreateView):
    model=CodeFile
    fields = ['title','file','comment']
    template_name='create.html'
    success_url=reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.role=='dev'



class UpdateFile(LoginRequiredMixin,UpdateView):
    model=CodeFile
    fields = ['title','file','comment']
    template_name='create.html'
    success_url=reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.role=='dev'
