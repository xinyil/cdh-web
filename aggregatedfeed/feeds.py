from django.db import models
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import timezone

from eventspages.models import EventPage
from mezzanine.blog.models import BlogPost

from itertools import chain
from datetime import datetime

class CombinedRecentFeed(Feed):
    title = 'News and Events at the Princeton CDH'
    link = 'http://digitalhumanities.princeton.edu'
    description = "News and Upcoming Events \
                   at the Princeton Center for Digital Humanities"

    def items(self):
        # Pull top 3 upcoming events, top 3 most recent blog posts and aggregate
        events = EventPage.objects.filter(status=2).exclude(event_data__event_end_time__lte=
                                           timezone.now())[:2]
        blogposts = BlogPost.objects.filter(status=2).order_by('-publish_date')[:3]
        return chain(events, blogposts) 
    
    # Each of these use a try / except model 
    # to ensure the appropriate data model is used
    def item_title(self, item):
        try:
            event_time = item.event_data.event_start_time

            fmt = '%d %b'
            event_time = event_time.strftime(fmt)

            title = item.event_data.event_title + " - " + event_time
            return title
        except:
            title = item.title
         
        finally:
            return title
    
    def item_description(self, item):
        try: 
            description = item.event_data.event_description

        except:
            description = item.description
        
        finally:
            return description
