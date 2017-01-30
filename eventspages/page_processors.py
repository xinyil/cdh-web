from .models import EventsLandingPage, EventPage
from mezzanine.pages.page_processors import processor_for

from django.utils.dateparse import parse_datetime


@processor_for(EventsLandingPage)
def pull_published_events(request, page):
    published_events = EventPage.objects.filter(status=2).filter(
         event_data__event_start_time__gte='2017-01-01'
    )
    return {'events': published_events}


@processor_for('events/fall-2016')
def pull_fall_2016_events(request, page):
    published_events = EventPage.objects.filter(status=2).filter(
        event_data__event_start_time__lt='2017-01-01'
    )
    return {'events': published_events}


