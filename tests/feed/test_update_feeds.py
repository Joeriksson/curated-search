from unittest.mock import patch, MagicMock

import pytest

from feed.management.commands.update_feeds import Command, get_aware_datetime
from feed.models import Feed, Entry


@patch.object(Command, 'update_feed')
@pytest.mark.django_db
def test_handle(mock_update_feed):
    feed1 = Feed.objects.create(feed_url='https://site1/rss/', active=True)
    feed2 = Feed.objects.create(feed_url='https://site2/rss/', active=False) # noqa
    command = Command()
    command.handle()
    mock_update_feed.assert_called_once_with(feed1)


@patch('feedparser.parse')
@patch.object(Command, 'update_feed_info')
@patch.object(Command, 'update_feed_entries')
@pytest.mark.django_db
def test_update_feed(mock_update_feed_entries, mock_update_feed_info, mock_parse):
    feed = Feed.objects.create()
    command = Command()
    command.update_feed(feed)
    mock_parse.assert_called_once_with(feed.feed_url)
    mock_update_feed_info.assert_called_once()
    mock_update_feed_entries.assert_called_once()


@pytest.mark.django_db
def test_update_feed_info():
    feed = Feed.objects.create()
    content = MagicMock()
    content.configure_mock(feed=MagicMock
        (
        title="Test Title",
        link="https://test.com",
        subtitle="Test Subtitle",
        updated="Mon, 20 Sep 2021 00:00:00 +0000"
    )
    )
    command = Command()
    command.update_feed_info(feed, content)
    assert feed.title == content.feed.title
    assert feed.site_url == content.feed.link
    assert feed.sub_title == content.feed.subtitle
    assert feed.site_updated == get_aware_datetime(content.feed.updated)


@pytest.mark.django_db
@patch.object(Command, 'update_entry')
def test_update_feed_entries(mock_update_entry):
    feed = Feed.objects.create()
    entries = [MagicMock(published="Mon, 20 Sep 2021 00:00:00 +0000"),
               MagicMock(published="Mon, 20 Sep 2021 00:00:00 +0000")]
    command = Command()
    command.update_feed_entries(feed, entries)
    assert mock_update_entry.call_count == len(entries)


@pytest.mark.django_db
def test_update_entry():
    feed = Feed.objects.create(feed_url='https://site1/rss/',
                               active=True,
                               site_updated="2021-02-01 00:00:00 +0000")
    entry = MagicMock(
        title="Test Title",
        link="https://test.com",
        subtitle="Test Subtitle",
        published="Mon, 20 Sep 2021 00:00:00 +0000"
    )
    entry.get.return_value = None
    command = Command()
    command.update_entry(feed, entry)
    obj = Entry.objects.get(link=entry.link)
    assert obj.title == entry.title
    assert obj.author == entry.get('author', None)
    assert obj.published == get_aware_datetime(entry.published)
    assert obj.tags == []
    assert obj.feed == feed
