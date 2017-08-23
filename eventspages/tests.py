from django.test import TestCase
from unittest.mock import Mock
from .models import Event, EventPage, EventsLandingPage
from datetime import datetime


class TestEventPageProcessors(TestCase):

    def setUp(self):
        event_dict = {
            'event_title': 'Foo',
            'event_description': 'Description here',
            'event_location': 'FooBar Hall',
        }

        event_page_dict = {
            'title': 'foobar',
            'status': 2
        }

        # An event starting on/after Aug 2017
        event_dict['event_start_time'] = datetime(
            year=2017,
            month=8,
            day=1,
        )
        event_dict['event_end_time'] = datetime(
            year=2017,
            month=8,
            day=2,
        )
        self.aug1 = Event.objects.create(**event_dict)
        EventPage.objects.create(event_data=self.aug1, **event_page_dict)
        # An event starting in Spring 2018
        event_dict['event_start_time'] = datetime(
            year=2018,
            month=1,
            day=31,
        )
        event_dict['event_end_time'] = datetime(
            year=2018,
            month=1,
            day=31,
        )
        self.jan31 = Event.objects.create(**event_dict)
        EventPage.objects.create(event_data=self.jan31, **event_page_dict)

        # An event for fall 2016
        event_dict['event_start_time'] = datetime(
            year=2016,
            month=8,
            day=1,
        )
        event_dict['event_end_time'] = datetime(
            year=2016,
            month=8,
            day=2,
        )
        self.aug8 = Event.objects.create(**event_dict)
        EventPage.objects.create(event_data=self.aug8, **event_page_dict)
        # An event for spring 2017
        event_dict['event_start_time'] = datetime(
            year=2017,
            month=3,
            day=20,
        )
        event_dict['event_end_time'] = datetime(
            year=2017,
            month=3,
            day=21,
        )
        self.mar20 = Event.objects.create(**event_dict)
        EventPage.objects.create(event_data=self.mar20, **event_page_dict)

        # Events pages
        events = EventsLandingPage.objects.create()
        events.set_slug('events')
        events.save()

        fall2016 = EventsLandingPage.objects.create()
        fall2016.set_slug('fall-2016')
        fall2016.set_parent(events)
        fall2016.save()

        spring2017 = EventsLandingPage.objects.create()
        spring2017.set_slug('spring-2017')
        spring2017.set_parent(events)
        spring2017.save()

        fall2017 = EventsLandingPage.objects.create()
        fall2017.set_slug('fall-2017')
        fall2017.set_parent(events)
        fall2017.save()

    def test_events(self):
        # 2 events for 2017 and 2018 upcoming
        response = self.client.get('/events/')
        assert len(response.context['events']) == 2

    def test_fall2017_events(self):
        # 1 event in fall 2017
        response = self.client.get('/events/fall-2017/')
        assert len(response.context['events']) == 1

    def test_spring2017_events(self):
        # 1 event in fall 2017
        response = self.client.get('/events/spring-2017/')
        assert len(response.context['events']) == 1

    def test_fall2016_events(self):
        # 1 event in fall 2017
        response = self.client.get('/events/fall-2016/')
        assert len(response.context['events']) == 1
