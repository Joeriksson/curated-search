from django.contrib import admin

from .models import Feed, Entry

admin.site.register(Feed)
admin.site.register(Entry)