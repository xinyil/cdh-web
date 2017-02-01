from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.utils.text import slugify
from .models import ProjectPage, ProjectMember, ProjectsLandingPage
from stocktemplate.models import StockLandingPage
from pprint import pprint


# Create your views here.



def display(request, title):

    research_page = StockLandingPage.objects.get(slug='research')
    
    for page in ProjectPage.objects.all():
        if  title == slugify(page.project_data.project_title):
            members = []
            for member in ProjectMember.objects.filter(project=page.project_data.id):
                members.append(member)
            return render(request, 'proj_page.html', {'project': page, 'members': members, 'page': research_page})
      
    raise Http404


