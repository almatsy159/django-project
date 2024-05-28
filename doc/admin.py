from django.contrib import admin

from .models import Document,Type,Content,Tag,Group
# Register your models here.

admin.site.register(Document)
admin.site.register(Type)
admin.site.register(Content)
admin.site.register(Tag)
admin.site.register(Group)