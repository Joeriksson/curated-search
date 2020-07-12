from django.core.management import BaseCommand
from feed.models import Feed, Entry

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    help = "Update Feeds into the database"

    def handle(self, *args, **options):
            # Implement the logic here
            pass