from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
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
    """
This class manages the display of search results in a list format.

It performs a full-text search on specific fields of the `Entry` model
using PostgreSQL's search capabilities. The search considers fields such as
`title`, `summary`, and `content`, weighted by relevance. Only results
with a significant rank are included, and they are sorted in descending
order of relevance.

Attributes:
    model (Entry): The model used for listing search results.
    context_object_name (str): The context variable name for the list of search results.
    template_name (str): The path to the template used to render the search results.

Methods:
    get_queryset(): Filters and ranks the `Entry` objects based on the search query.
"""

    model = Entry
    context_object_name = "entries"
    template_name = "feed/search.html"

    def get_queryset(self):
        """
        Constructs and returns a queryset of `Entry` objects based on a search query.

        This method processes the GET parameter `q` from the request. If a query is
        provided, it builds a search vector combining weighted fields such as `title`,
        `summary`, and `content`, and uses a search query to calculate a rank based on
        the relevance of these fields. Entries with a rank greater than zero are
        filtered and ordered in descending order by rank. If no search query is present,
        an empty queryset is returned.

        :param self: The instance of the current view.
        :return: A queryset of `Entry` objects annotated with a rank and filtered by
                 relevance to the search query. If no query is specified, an empty
                 queryset is returned.
        :rtype: QuerySet
        """
        if query := self.request.GET.get("q"):
            search_vector = (
                    SearchVector("title", weight="A") +
                    SearchVector("summary", weight="B") +
                    SearchVector("content", weight="C")
            )
            search_query = SearchQuery(query)
            rank = SearchRank(search_vector, search_query)
            return Entry.objects.annotate(
                rank=rank
            ).filter(
                rank__gt=0  # Ensures only relevant results are included
            ).order_by("-rank")  # Order by the highest rank first
        return Entry.objects.none()
