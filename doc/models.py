from django.db import models
from django.utils import timezone
import os

# Create your models here.
        



"""
css_lambda = File("style",".css","doc/static/")
print(css_lambda.read_file())
"""
class File(models.Model):
    #url = models.CharField(default="./static",max_length=5)
    url = models.URLField()
    content = models.TextField()
    
class Type(models.Model):
    name = models.CharField(max_length=50)
    proc = models.CharField(max_length=50)
    
    @classmethod
    def create(cls,name,proc):
        item = cls(name,proc)
        # do something with the created item
        return item
    def __str__(self):
        return self.name
    
    

class Content(models.Model):
    content_type = models.ForeignKey(Type,on_delete=models.CASCADE)
    #content_text = models.CharField(max_length=200)
    content = ""
    def __str__(self):
        return self.content
    
    def add_content(content):
        Content.content = content
    
    @classmethod
    def create(cls,type):
        item = cls(type)
        # do something with the created item
        return item
    
class Group(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def create(cls,name,level):
        item = cls(name,level)
        # do something 
        return item

class MetaDoc(models.Model):
    name = models.CharField(max_length=50)
    struct = models.CharField(max_length=10,default=None)

class Document(models.Model):
    #group_id = models.ForeignKey(Group,on_delete=models.CASCADE)
    #meta_doc_id = models.IntegerField(default=0) 
    title = models.CharField(max_length=40,default="")
    #content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
    content = models.CharField(max_length=100,default="")
    date = models.DateField("date creation",default=timezone.now)
    link = models.URLField()
    #image = models.ImageField()
    #tag = models.ManyToManyRel(Tag)
    
    def __str__(self):
        res = f"{self.title} at {self.date} toward {self.link}"
        return res

    def add_tag(self,name,group=None):
        tag = Tag(group,name,self.id)
        tag.save()
        print(f"{tag.id} created")
        #insert tag here !
        return tag.id
    """
    @classmethod
    def create(cls,title,content_id,group_id,date,link):
        item = cls(group_id,title,content_id,date,link)
        # do something with the created item
        return item
    """
class Tag(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=30,default="")
    doc_id = models.ForeignKey(Document,on_delete=models.CASCADE,default=0)
    is_group = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} belong to {self.group}"
    
    def belong_to(self,group=None):
        if group == self.group:
            return True
        else :
            return False
    def get_all(self,document):
        tag_list = Tag.objects.filter(doc_id = document)
        return tag_list
    
    def create_group(self):
        self.is_group = True
        self.group = Group(self.name) 
        
    @classmethod
    def create(cls,name,group,doc_id,is_g=False):
        item = cls(name,group,doc_id,is_g)
        # do something with the created item
        return item
    
class Liste(models.Model):
    name = models.CharField(max_length=50)
    
class Fiche(models.Model):
    name = models.CharField(max_length=50)
    
    def get_items(self):
        self.name
    
class List_Item(models.Model):
    name = models.CharField(max_length=50)
    typ = models.CharField(max_length=50)
    id_list = models.ForeignKey(Liste,on_delete=models.CASCADE)
        
class Fiche_Item(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    id_fiche = models.ForeignKey(Fiche,on_delete=models.CASCADE)