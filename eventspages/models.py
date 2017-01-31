from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core import fields
from mezzanine.core.models import Displayable
from mezzanine.core.fields import RichTextField, FileField

from django.utils import timezone


# Create your models here

class Event(models.Model):
    event_title = models.CharField(max_length=80)
    event_description = fields.RichTextField()
    event_sponsor = models.CharField(max_length=80, null=True, blank=True)
    event_image  = FileField("Image", format="Image", blank=True, null=True)
    event_location = models.TextField(max_length=225)
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField()


    def is_elapsed(self):
        return self.event_start_time <= timezone.now()

    def __str__(self):
        return self.event_title + " " + \
        self.event_start_time.strftime('%b %d, %Y')


class EventPage(Displayable):
    event_data = models.ForeignKey(Event)
    extra_info = fields.RichTextField()
    title = models.CharField(max_length=500, default='Events @ CDH') 
    def get_absolute_url(self):
        return '/events/' + str(self.pk)

    class Meta:
        ordering = ('event_data__event_start_time',)


class EventsLandingPage(Page):
    class Meta:
        verbose_name = 'Event List'
