from django.contrib import admin

from .models import Feed, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'published', 'feed', 'added', 'edited']
    list_filter = ['published', 'added', 'edited', 'feed__title']
    search_fields = ('title',)


class FeedAdmin(admin.ModelAdmin):
    list_display = ['title', 'feed_url', 'site_url', 'added', 'edited', 'active']
    list_filter = ['added', 'site_updated', 'added']
    search_fields = ('title',)

admin.site.register(Feed, FeedAdmin)
admin.site.register(Entry, EntryAdmin)