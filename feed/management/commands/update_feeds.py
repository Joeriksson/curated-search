from datetime import datetime

import feedparser
from django.core.management import BaseCommand
from django.utils.timezone import is_aware, make_aware

from feed.models import Feed, Entry


def get_aware_datetime(date_str):
    result = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
    if not is_aware(result):
        result = make_aware(result)
    return result


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    help = "Update Feeds into the database"

    def handle(self, *args, **options):
        feeds = Feed.objects.all()
        for feed in feeds:
            if feed.active:
                self.update_feed(feed)

    def update_feed(self, feed):
        """Update a single feed."""
        content = feedparser.parse(feed.feed_url)
        self.update_feed_info(feed, content)
        self.update_feed_entries(feed, content.entries)

    def update_feed_info(self, feed, content):
        """Update the information of a feed."""
        feed.title = content.feed.title
        feed.site_url = content.feed.link
        feed.sub_title = content.feed.subtitle
        feed.site_updated = get_aware_datetime(content.feed.updated)
        feed.save()

    def update_feed_entries(self, feed, entries):
        """Update the entries of a feed."""
        for entry in entries:
            self.update_entry(feed, entry)

    def update_entry(self, feed, entry):
        """Update a single entry of a feed."""
        tags = entry.get('tags', None)
        tag_list = [tag.get('term') for tag in tags] if tags else []
        obj, created = Entry.objects.update_or_create(
            link=entry.link,
            defaults={
                'title': entry.title,
                'author': entry.get('author', None),
                'published': get_aware_datetime(entry.published),
                'tags': tag_list,
                'feed': feed,
            },
        )
        obj.save()
