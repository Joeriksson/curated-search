from django.core.management import BaseCommand

from newspaper import Article

from feed.models import Entry

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    help = "Update Article Content into the database"

    def handle(self, *args, **options):

        entries = Entry.objects.all()

        for entry in entries:
            if not entry.feed.active:
                continue

            article = Article(entry.link)
            article.download()
            article.parse()

            entry.content = article.text
            if article.meta_description:
                entry.summary = article.meta_description
            # if article.tags:
            #     entry.tags = article.tags

            entry.save()
