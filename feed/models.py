import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class TimeStampedModel(models.Model):
    added = models.DateTimeField(auto_now_add=True, db_index=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Feed(TimeStampedModel):
    feed_url = models.URLField(max_length=256, primary_key=True)
    title = models.CharField(max_length=200, blank=True)
    sub_title = models.CharField(max_length=300, blank=True)
    site_url = models.URLField(max_length=256, blank=True)
    site_updated = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Title: {self.title} - Url: {self.site_url}'

    class Meta:
        ordering = ['-added']
        verbose_name_plural = "feeds"


class Entry(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    link = models.URLField(max_length=256)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=200, null=True)
    published = models.DateTimeField()
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    # TBD Fix misspelling of entries with an empty db
    feed = models.ForeignKey(Feed, related_name='entries', on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title} - Feed: {self.feed.title}'

    class Meta:
        ordering = ['-added']
        verbose_name_plural = "entries"
