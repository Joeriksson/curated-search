import pytest

from django.utils import timezone

from feed.models import Feed, Entry


@pytest.mark.django_db
def test_feed_model():
    now = timezone.now()
    feed = Feed(
        feed_url='https://example.org/rss.xml',
        title='Test feed',
        sub_title='Test subtitle',
        site_url='https://example.org',
        site_updated=now,
    )
    feed.save()

    feed.refresh_from_db()

    assert feed.feed_url == 'https://example.org/rss.xml'
    assert feed.title == 'Test feed'
    assert feed.sub_title == 'Test subtitle'
    assert feed.site_url == 'https://example.org'
    assert feed.site_updated == now
    assert str(feed) == f'Title: {feed.title} - Url: {feed.site_url}'


@pytest.mark.django_db
def test_entry_model():
    now = timezone.now()
    feed = Feed(
        feed_url='https://example.org/rss.xml',
        title='Test feed',
        sub_title='Test subtitle',
        site_url='https://example.org',
        site_updated=now,
    )
    feed.save()

    entry = Entry(
        title='A test article',
        link='https://example.org/testarticle/',
        summary='This is a summary of the article',
        author='John Doe',
        published=now,
        tags=['test1', 'test2'],
        feed=feed,
    )

    entry.save()

    entry.refresh_from_db()

    assert entry.title == 'A test article'
    assert entry.link == 'https://example.org/testarticle/'
    assert entry.summary == 'This is a summary of the article'
    assert entry.author == 'John Doe'
    assert entry.published == now
    assert entry.tags == ['test1', 'test2']
    assert entry.feed == feed
