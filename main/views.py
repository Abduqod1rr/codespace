from django.shortcuts import render
from .models import CodeFile
from django.urls import reverse_lazy
from django.views.generic import CreateView ,DeleteView ,ListView   ,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


from django.db.models import Q

class CodeFileListView(ListView):
    model = CodeFile
    template_name = "home.html"
    context_object_name = 'object_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(comment__icontains=query) |
                Q(dev__username__icontains=query)
            )
        
        return queryset.order_by('-created_at')

class CreateFile(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model=CodeFile
    fields = ['title','file','comment']
    template_name='create.html'
    success_url=reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.role=='dev'
    
    def form_valid(self, form):
        form.instance.dev=self.request.user
        return super().form_valid(form)





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
        
    
def search(request):
    query = request.GET.get('q')
    if query:
        
        result= CodeFile.objects.filter(title__icontains=query)
    else:
        result= CodeFile.objects.none()
    
    return render(request, 'search_results.html', {'results': result})