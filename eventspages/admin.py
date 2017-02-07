from django.contrib import admin
from .models import Event, EventPage, EventsLandingPage


class EventPageInline(admin.StackedInline):
    model = EventPage
    max_num = 1
    fields = ('title', 'status', 'publish_date', 'expiry_date')


class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventPageInline
            ]


# Register your models here.a
admin.site.register(Event, EventAdmin)
admin.site.register(EventsLandingPage)
