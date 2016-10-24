from mezzanine.pages.page_processors import processor_for
from .models import StaffLandingPage, StafferPage

@processor_for(StaffLandingPage)
def get_staffers(request, page):
    staffers = StafferPage.objects.filter(status=2)
    return {'staffers': staffers}
