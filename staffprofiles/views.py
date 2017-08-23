from django.shortcuts import render
from .models import Staffer, StafferPage, Specialty
from stocktemplate.models import StockLandingPage
from django.http import Http404

# Create your views here.

def generate_stafferpage(request, name):

    # Create list of all published staff pages
    q = StafferPage.objects.filter(status=2)

    # Create a Page context under the about heading for the side menu
    page_context = StockLandingPage.objects.get(slug='about')
    staffer = None

    # Match the url with the staffer name
    for page in q:
        if page.staffer_data.name.lower().replace(' ', '-') == name:
            staffer = page

    # Raise 404
    if not staffer:
        raise Http404

    # Generate a list of specialties linked to the staffer
    specialties = Specialty.objects.filter(staff_member__id=staffer.staffer_data.id)

    return render(request, 'staffer_page.html', {'staffer': staffer,
                  'page': page_context, 'specialties': specialties, })
