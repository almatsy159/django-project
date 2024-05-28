from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import RView 

# import model cclass

# Create your views here.

#arguments : 
#   type:"liste => No Id,fiche=> Id," page ? => multiple , autre ... definitely ! V
#   name :"table" => if exist => view of result , else view of page of this name ?
#   

def index_single(request,arguments=None):
    if arguments != None:
        #check type !!!
        page_name = arguments[0]
        page_type = arguments[1]
        my_arg={}
        k = 2
        for k in arguments:
            my_arg={str(k):k} 
        if page_name == "liste":
            #item = CClass.objects()
            print(page_name="list")
            
            
def index(request,arguments=None):
    # get tables
    lst_a = ["0","1","2","3","4","5"]
    lst_b = ["a","b","c","d","e","f"]
    lists = [lst_a,lst_b]
    print(lists)
    
    context={"lists":lists,"request":request,"arguments":arguments}
    # return HttpRequest(render,"single/index.html",context)
    return render(request,"single/index.html",context)

    
            
    
