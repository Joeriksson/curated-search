from django.contrib.postgres.search import SearchVector
from django.core.management import call_command
from django.http import HttpResponse
from django.views.generic import View, ListView

from feed.models import Entry


class UpdateFeedView(View):
    def get(self, *args, **kwargs):
        call_command("update_feeds")

        return HttpResponse("OK")


class UpdateContentView(View):
    def get(self, *args, **kwargs):
        call_command("update_content")

        return HttpResponse("OK")


class SearchResultsList(ListView):
    model = Entry
    context_object_name = "entries"
    template_name = "feed/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        # return Quote.objects.filter(
        #     quote__search=query
        # )
        return Entry.objects.annotate(
            search=SearchVector("title", "summary", "content")
        ).filter(search=query)
