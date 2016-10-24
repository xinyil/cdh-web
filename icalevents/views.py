from django.shortcuts import render
from eventspages.models import Event
from django.http import Http404, HttpResponse

from pytz import timezone
import vobject


def return_ical(request, pk):

    eastern = timezone('US/Eastern')

    try:
        event = Event.objects.get(pk=pk)
        print("Found an event")
    except:
        print("Returning a 404")
        return Http404()

    cal = vobject.iCalendar()
    cal.add('method').value = 'PUBLISH'

    cal.add('vevent')
   
    summary = cal.vevent.add('summary')
    summary.value = event.event_title

    start = cal.vevent.add('dtstart')
    start.value = event.event_start_time.astimezone(eastern)
    
    end = cal.vevent.add('dtend')
    end.value = event.event_end_time.astimezone(eastern)

    location = cal.vevent.add('location')
    location.value = event.event_location

    icalstream = cal.serialize()

    response = HttpResponse(icalstream, content_type='text/calendar')
    response['Filename'] = event.event_title+'.ics'
    response['Content-Disposition'] = 'attachment; filename="'+event.event_title+'.ics"'

    return response
