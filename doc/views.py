from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.utils import timezone as tz
from flask import request,jsonify
#from django.template import loader
#importer les classes
from .models import Document,Tag,Content,File
import os
from rest_framework import routers,serializers,viewsets
"""
from django.contrib.auth.models import User,Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email',"groups"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields=['url','name']

# view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =UserSerializer
    
class GroupViewSet(viewsets.ModelViewSet):
    ""API ENDPOINT""
    queryset = Group.objects.all()
    serializer_class=GroupSerializer
    
"""

class DocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['title','content','date','link']
        

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['url','content']

class FileViewSet(viewsets.ModelViewSet):
    "API ENDPOINT"
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
class DocViewSet(viewsets.ModelViewSet):
    "API ENDPOINT"
    queryset = Document.objects.all()
    serializer_class = DocSerializer

# view.py.index = index.py => index.html
# Create your views here.
def get_form():
    return HttpResponse("<p>form here</p>")



def index(request,args=None):
    context = {}
    if args == None:
        args = {}
    else:
        print(f"arg type : {type(args)}")
        if type(args) == dict:
            #print("is dict ! ")
            for k,v in args.items():
                context[k] = v
    context["args"]=args
    #if args:
    #    context={"args":args}
    #else :
    #    context={"args":"no args"}
    #name = "index"
    print(f"context : {context}")
    doc_list = Document.objects.all()
    """
    for d in doc_list:
        
        flag = 0
        t = Tag.objects.filter(pk=d.id)
        if t:
            flag = 1
            #tags={d.id:t}
            doc_tag = {d.id:t}
    """
            
    #print(doc_list)
    #res = request
    #res =",".join([d.title for d in doc_list])
    #print(HttpResponse(res))
    #template = loader.get_template("doc/index.html")
    """
    if request == None:
        res += "no request send"
    else :
        res += f"{request}"
    """
    #tag_list = Tag.objects.order_by("id")[:10]
    context["doc_list"] = doc_list
    print(request)
    
    return render(request,"doc/index.html",context)
    #return HttpResponse(request,context)

def second(request,args=None):
    header = ""
    path = os.getcwd()
    info = os.listdir()
    # in a view.py , you could call generator of view.html  and then load it. 
    # the last call is still stored so if it couldn't gen it return the last with this name generated ...
    
    #with open("./doc/templates/header.html","r") as f:
    #    header += f.readlines
    context = {"info":info,"path":path,"args":args,"header":header}
        
    return render(request,"doc/second.html",context)

def others(request,arg=None):
    liste = [1,2,3,4,5,6,7,8,9,10]
    main = {"name":"other"}
    fiche = {"name":"fiche","value":10,"content":"lorem ipsum"}
    page = {"title":"others"}
    print(arg)
    form_list = {"form_list":{"name":"list_name"}}
    form_fiche = {"form_fiche":{"name":"fiche_name"}}
    dirs = os.listdir()
    menu = {"dirs":dirs}
    context={"liste":liste,"arg":arg,"fiche":fiche,"page":page,"get_form":get_form,
            "form_fiche":form_fiche,"form_list":form_list,"menu":menu}
    return render(request,"doc/others.html",context)

def detail(request,document_id=None):
    #context={}
    """
    try:
        document = Document.objects.get(pk=document_id)
        context["document":document]
        
    except Document.DoesNotExist:
        context["error":Document.DoesNotExist]
        raise Http404(f"Question does not exist looking for {document_id}")
    
    return render(request,"doc/detail.html/", {"document": document})
    
    """
    name = "detail"
    print(document_id,request)
    if document_id != None: 
        """
        try:
            document = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            document = Document()
        """
        document = get_object_or_404(Document,pk=document_id)
        #tag = Document.objects.filter(tag_name=document_id) 
        #print(f"object get {object}")
        
        #document_list= Document.objects.order_by("id")
        #print(f"doc list :{document_list}")
        #context={"document_list":document_list}
        tags = Tag.objects.filter(pk=document_id)
        context={"name":name,"tags":tags,"document":document}
    else:
        document_list = Document.objects.order_by("id")
        last_id = Document.objects.last().id
        next_id = last_id + 1
        context={"name":name,"next_id":next_id,"document_list":document_list}
        #res = render(request,"doc/detail.html")
        #context={"document":document,"tags":tag,"content":content}
        
    return render(request,"doc/detail.html",context)

def tag(request,tag_id=None):
    if tag_id != None:
        tag = get_object_or_404(Tag,pk=tag_id)
        context = {"tag":tag}
    else:
        tag_list =Tag.objects.order_by("id")
        context = {"tag_list":tag_list}
    return render(request,"doc/tag.html",context)

def content(request):
    content =Content.objects.order_by("id")
    context = {"content":content}
    return render(request,"doc/content.html",context)
    
def test(request,context):
    return render(request,"doc/test.html",context)

def group(request,context):
    return render(request,"doc/group.html",context)


def create_tag(request,id):
    #print(context)
    #d = Document.objects.filter(pk=id)
    #t = Tag.objects.create()
    context ={}
    t= Tag(name="a",doc_id=id,group=None,is_group=True)
    t.document_id.set(id)
    t.save()
    #context={"tag":t}
    #context = {"document_id":doc_id,"t":t}
    return render(request,"doc/detail.html",context)
    #return HttpResponse(f"create tag with this id :{id}")
    res = detail(request,id)
    print(res)
    return res

def other(request,arg):
    context= {"arg",arg}
    return render(request,"other/",context)

def first(request,arg):
    context={"arg":arg}
    return render(request,"first/",context)

def call_from_index(request):
    request_p = request.GET 
    #print(f"x:{x}")
    args = {}
    #for i in request_p:
    #    print(i)
    for n,p in request_p.items():
        args[n] = p
    #print(f"fname : {request.fname}")
    #flag_args = False
    #if args == None:
        #args = "call_from_index"
    #else : 
        #args += " original arg"
        #flag_args = True
    print(f"arg : {args}")
    name = args["ftitle"]
    content = args["fcontent"]
    link = args["flink"]
    date = tz.now()
    try :
        d = Document(title=name,content=content,link=link,date=date)
        d.save()
    except Http404:
        d = None
    
    args["d"] = d    
    res = index(request,args)
    
    #context = {"args":args}
    return res
    #return render(request,"doc/index/",context)
    
def api(request,*args):
    
    context ={}
    #extra = request.get("extra")
    
    #context["extra"] = extra
    context["arg"]=args
    
    return render(request,"doc/api.html",context)
    #return jsonify(context)
    
    
