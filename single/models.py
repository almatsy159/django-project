from django.db import models
import os

# Create your models here.

# Model / Views / Liste / Fiche / Page...  

# all class must be formated according to the index views.
# initiated as django need it , i'm not sure if the structure is well adapted to add other prop or __init__ condition,
# type of class seem to solve this probleme as you can use the django like object 
class Data:
    #check other code =>mime,value, else? binary, img,text ... data was a choice by default 2 categories(Page? => Index) seem not necessary right now
    pass

class Card(models.Model):
    #see form doc . py
    # card has a repr made with bs  
    pass
    
class List(models.Model):
    # shoud code a minimal code ...
    # well handled in edit doc but should be recoded
    # list should handle multiple type (so define a struct by types:args?)
    # summary of card !!! list += list_item <= document
    name = models.CharField(max_length=10)
    structure = models.CharField(max_length=50)

class ListItem(models.Model):
    name = models.CharField("", max_length=50)
    lst_id = models.ForeignKey(List,on_delete=models.CASCADE)
    

class Page:
    # should be defined wisely ,even the name could change ... some work about it already ... maybe a system ?
    # import html by launching.py 
    # composition of list and card and data 
    pass
    
class RView :
    # reworked view
    # call django views object.
    # arguments is partially described in views.py(single)
    # should gen a view django like fonction !!!
    def __init__(self,name,request,arguments):
        
        self.res = f"def {name}({request},{arguments}):\n"
        
        self.res += "\treturn "

class RModel :
    def __init__(self):
        # need to access to the base structure and not table ...
        # to make this create a fonction that connect to the django db threw sql and for table in "show db" :"show cols"
        # should generate a django like class
        # call django.model object (and return it ? => call method that return model)
        # class : 
        # - fields ( "args")
        # - method( "fcts")
        """
            class Model0(models):
                {name} = CharField
                {}...
        """
        pass

class RIndex:
    pass
    
class ToC:
    #type of content
    types = {0:"Card",1:"List",2:"Page",3:"Data"}
    # 0 : card ; a card have an id, (belong to a list if it has a name also?)=> page
    # 1 : list ; a list only need a name
    """
        if you try to create a class with both id and name => its a card that belong to a list
        elif with only a name , it's a list !
        elif with only an id , then it's a page , not owned by a list (should be rare case only)
        else it has no name nor id : then its data ?
    """
    def __init__(self,name=None,val=None):
        if name == None and val == None:
            id = 3
            obj = Data()
        elif name == None :
            if val != None:
                id = 0
                obj = Card()
            else :
                id = 2
                obj = Page()
        elif id == None:
            id = 1
            obj = List()
        res = (id,obj)
        
        
class CClass():
    # view, model, other ...call a class from a struct (name/id;args)
    def __init__(name,id):
        pass
    