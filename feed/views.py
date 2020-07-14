from django.shortcuts import render

from django.views.generic import View
from django.core.management import call_command
from django.http import HttpResponse

class UpdateFeedView(View):

    def get(self, *args, **kwargs):
        call_command('update_feeds')

        return HttpResponse('OK')


class UpdateContentView(View):

    def get(self, *args, **kwargs):
        call_command('update_content')

        return HttpResponse('OK')


