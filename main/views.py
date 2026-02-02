from django.shortcuts import render
from .models import CodeFile
from django.urls import reverse_lazy
from django.views.generic import CreateView ,DeleteView ,ListView   ,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


class CodeFileListView(ListView):
    model = CodeFile
    template_name = "home.html"



class CreateFile(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model=CodeFile
    fields = ['title','file','comment']
    template_name='create.html'
    success_url=reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.role=='dev'
    
    def form_valid(self, form):
        form.instance.dev=self.request.user
        return super().form_valid



class UpdateFile(LoginRequiredMixin,UpdateView):
    model=CodeFile
    fields = ['title','file','comment']
    template_name='create.html'
    success_url=reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.role=='dev'



class FileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CodeFile
    template_name = 'delete.html'
    success_url= reverse_lazy('home')
    
    def test_func(self):
        return self.request.user == self.get_object().dev
        
    