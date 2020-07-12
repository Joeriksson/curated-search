from datetime import datetime
import pytest

from django.utils import timezone

from feed.models import Feed, Entry


@pytest.mark.django_db
def test_feed_model():
    feed = Feed(
        feed_url='https://example.org/rss.xml',
        title='Test feed',
        sub_title='Test subtitle',
        site_url='https://example.org',
        site_updated=timezone.now()
    )
    feed.save()

    assert feed.feed_url == 'https://example.org/rss.xml'
    assert feed.title == 'Test feed'
    assert feed.sub_title == 'Test subtitle'
    assert feed.site_url == 'https://example.org'
    assert isinstance(feed.site_updated, datetime)
    assert str(feed) == f'Title: {feed.title} - Url: {feed.site_url}'
