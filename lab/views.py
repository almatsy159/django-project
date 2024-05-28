from django.shortcuts import render
from django.views import generic
#from .models import Work

# Create your views here.

def index(request):
    context={}
    return render(request,"lab/index.html",context)

"""
class IndexView(generic.ListView):
    template_name = "lab/index.html"
    context_object_name = "latest_work"
    
    def get_queryset(self):
        return None
    
class DetailView(generic.DetailView):
    template_name = "lab/detail.html"
    #model = Work    
"""
