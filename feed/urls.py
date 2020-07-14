from django.urls import path

from .views import UpdateFeedView, UpdateContentView


urlpatterns = [
    path('feed/', UpdateFeedView.as_view(), name='update_feeds'),
    path('content/', UpdateContentView.as_view(), name='update_content'),
]