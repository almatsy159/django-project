"""
URL configuration for MyOwnSpace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


from django.contrib.auth.models import User,Group
from rest_framework import routers,serializers,viewsets
from doc  import views,models

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
    #""API ENDPOINT""
    queryset = Group.objects.all()
    serializer_class=GroupSerializer
    

# determine automatically url conf
router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'documents',views.DocViewSet)
router.register(r'files',views.FileViewSet)



#path("/","root.urls",name="root")
my_dic = {"name":"args"} 
urlpatterns = [
    path('', include(router.urls)),
    path("single/",include("single.urls"),name="single"),
    path("doc/",include("doc.urls"),name="doc"), 
    path("polls/", include("polls.urls"),name="polls"),
    path('admin/', admin.site.urls),
    path('lab/',include("lab.urls"),name="lab")
]

#    path('doc/api-auth', include('rest_framework.urls')),