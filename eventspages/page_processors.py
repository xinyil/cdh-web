from .models import EventsLandingPage, EventPage
from mezzanine.pages.page_processors import processor_for

@processor_for(EventsLandingPage)
def pull_published_events(request, page):
    published_events  = EventPage.objects.filter(status=2)
    return {'events': published_events}
     


