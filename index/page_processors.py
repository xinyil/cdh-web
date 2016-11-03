from eventspages.models import EventPage, Event
from projectpages.models import ProjectPage
from mezzanine.pages.page_processors import processor_for
import random



@processor_for('/')
def provide_context_frontpage(request, page):

    events = Event.objects.all()
    future_event_id = []
    for event in events:
        if event.is_elapsed() is False:
            future_event_id.append(event.id)

    published_events = EventPage.objects.filter(status=2).filter(
                        event_data__id__in=future_event_id)

    published_events = published_events[:3]

    published_projects = ProjectPage.objects.filter(status=2)
    # don't error when there aren't projects available
    if published_projects:
        ids = ProjectPage.objects.filter(status=2).values_list('id', flat=True)

        # FIXME: technically still will error for less than 3 projects
        random_ids = random.sample(list(ids), 3)
        published_projects = published_projects.filter(id__in=random_ids)

    return {'events': published_events, 'projects': published_projects}

