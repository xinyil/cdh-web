from django.contrib import admin
from .models import Event, EventPage, EventsLandingPage

# Register your models here.a
admin.site.register(Event)
admin.site.register(EventPage)
admin.site.register(EventsLandingPage)
