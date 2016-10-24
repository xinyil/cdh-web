from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import EventPage, EventsLandingPage


# Create your views here.
def display_event(request, pk):
    eventpage = EventPage.objects.get(pk=pk)
    event = eventpage.event_data

    events_context = EventsLandingPage.objects.get(slug='events')



    return render(request, 'event.html', {
        'event': event, 'page': events_context}) 
