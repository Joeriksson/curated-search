from django.urls import path

from .views import UpdateFeedView, UpdateContentView, SearchResultsList

urlpatterns = [
    path('feed/', UpdateFeedView.as_view(), name='update_feeds'),
    path('content/', UpdateContentView.as_view(), name='update_content'),
    path("search/", SearchResultsList.as_view(), name="search_results"),
]