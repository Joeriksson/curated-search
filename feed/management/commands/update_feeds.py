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
        # Implement the logic here
        feeds = Feed.objects.all()

        for feed in feeds:
            print(feed.feed_url)

            if not feed.active:
                continue

            content = feedparser.parse(feed.feed_url)

            current_feed = Feed.objects.get(feed_url=feed.feed_url)

            current_feed.title = content.feed.title
            current_feed.site_url = content.feed.link
            current_feed.sub_title = content.feed.subtitle
            current_feed.site_updated = get_aware_datetime(content.feed.updated)

            current_feed.save()

            for entry in content.entries:

                tags = entry.get('tags', None)

                if tags:
                    tag_list = [tag.get('term') for tag in tags]

                obj, created = Entry.objects.update_or_create(
                    link=entry.link,
                    defaults={
                        'title': entry.title,
                        'summary': entry.summary,
                        'author': entry.get('author', None),
                        'published': get_aware_datetime(entry.published),
                        'tags': tag_list,
                        'feed': current_feed,
                    },
                )

                obj.save()
