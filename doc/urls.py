from django.urls import path

from . import views
# path("./<int:doc_id>/",view="detail"),
urlpatterns = [
    path("other/",views.other,name="other"),
    path("first/",views.first,name="first"),
    path("detail/",views.detail,name="detail"),
    path("detail/<int:document_id>/",views.detail,name="detail"),
    path("tag/",views.tag,name="tag"),
    path("tag/<int:tag_id>",views.tag,name="tag"),
    path("content/<int:content_id>/",views.content,name="content"),
    path("group/",views.group,name="group"),
    path("", views.index,name="index"),
    path("<int:document_id>",views.detail,name="detail"),
    path("others/",views.others,name="others"),
    path("second/",views.second,name="second"),
    path("call_from_index/",views.call_from_index,name="call_from_index"),
    path("api/",views.api,name="api")
]

#path("call_from_index/<slug:slug>",views.index,name="index")