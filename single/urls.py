from django.urls import path

from . import views
# path("./<int:doc_id>/",view="detail"),
urlpatterns = [
    path("", views.index,name="index")
]