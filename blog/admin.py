from django.contrib import admin
from .models import Post

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Post,EntryAdmin)