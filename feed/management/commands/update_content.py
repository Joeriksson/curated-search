import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand

from feed.models import Entry

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    help = "Update Article Content into the database"

    def handle(self, *args, **options):

        entries = Entry.objects.all()

        for entry in entries:
            if not entry.feed.active:
                continue

            article_url = entry.link

            response = requests.get(article_url, headers=HEADERS)
            html = response.text
            soup = BeautifulSoup(html, "html.parser")

            paragraphs = soup.find_all('p')

            article_content = ''
            for paragraph in paragraphs:
                article_content += paragraph.text
                # print(p.text)

            entry.content = article_content
            entry.save()
