from django.shortcuts import render

# Create your views here.
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *

from django.urls import reverse_lazy

class Home(View):
    def get(self,request):
        return render(request,'app/home.html')


class SchoolListView(ListView):
    model=School                 # collected all objects of School model
    context_object_name='schools'
    #template_name='app/school_list.html'
    ordering=['name']

class SchoolDetailView(DetailView):
    model=School
    context_object_name='school'
    
class SchoolCreateView(CreateView):
    model=School
    fields='__all__'

class SchoolUpdateView(UpdateView):
    model=School
    fields='__all__'




class SchoolDeleteView(DeleteView):
    model=School
    context_object_name='school'
    success_url=reverse_lazy('list')

















    