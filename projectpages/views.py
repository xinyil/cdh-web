from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import ProjectPage, ProjectMember, ProjectsLandingPage
from stocktemplate.models import StockLandingPage
from pprint import pprint


# Create your views here.



def display(request, title):

    research_page = StockLandingPage.objects.get(slug='research')
    pprint(vars(research_page))
    
    for page in ProjectPage.objects.all():
        if page.project_data.project_title.replace(' ', '').lower() == title.lower():
            members = []
            for member in ProjectMember.objects.filter(project=page.project_data.id):
                members.append(member)
            return render(request, 'proj_page.html', {'project': page, 'members': members, 'page': research_page})
      
    return HttpResponse('Woot!')    


