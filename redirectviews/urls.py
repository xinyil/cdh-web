from django.conf.urls import url
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^people/', RedirectView.as_view(url='/about/staff/', permanent=True),
        name='staff-redirect'),
    url(r'^groups/', RedirectView.as_view(url='/community/', permanent=True),
        name='group-redirect'),
    url(r'calendar/', RedirectView.as_view(url='/events/', permanent=True),
        name='calendar-redirect'),
    url(r'^directions/', RedirectView.as_view(url='/contact/', permanent=True),
        name='directions-redirect'),
    url(r'^feed/', RedirectView.as_view(url='/latest/feed/', permanent=True),
        name='RSS-feed'),
    url(r'^new/', RedirectView.as_view(url='/resources/new-to-dh/', permanent=True),
        name='New-to-DH'),
]
