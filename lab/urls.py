from django.urls import path

from . import views
# path("./<int:doc_id>/",view="detail"),
urlpatterns = [
    path("",views.index,name="index")
    ]
    
"""
    path("", views.IndexView.as_view(),name="index"),
    path("<str:table>/<int:pk>/",views.DetailView.as_view(),name="details"),
    path("<str:table>/",views.ListView.as_view(),name="liste")
]
"""