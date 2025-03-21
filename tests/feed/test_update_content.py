import re
from unittest.mock import patch, MagicMock

import pytest
from newspaper import Article

from feed.management.commands.update_content import Command
from feed.models import Feed, Entry


@pytest.mark.django_db
@patch.object(Article, "download")
@patch.object(Article, "parse")
def test_handle(mock_parse, mock_download):
    # Create a feed and an associated entry
    feed = Feed.objects.create(active=True, feed_url="https://test.com")
    entry = Entry.objects.create(
        feed=feed,
        link="https://test.com",
        published="2021-09-20 00:00:00+00:00",
        content="<h1>Test Content</h1>",
    )

    # Create a MagicMock for the Article object with HTML in the text
    mock_article = MagicMock()
    mock_article.text = "<p>Test Content with <strong>HTML</strong> tags</p>"

    # Configure the Article constructor to return the mock_article
    with patch("newspaper.Article", return_value=mock_article):
        command = Command()
        command.handle()

    # Refresh the entry from the database
    entry.refresh_from_db()

    # Check that the entry's content was updated and does not contain any HTML tags
    html_tag_pattern = re.compile("<.*?>")
    assert not bool(html_tag_pattern.search(entry.content))
