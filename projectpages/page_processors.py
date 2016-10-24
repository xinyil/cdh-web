from .models import ProjectsLandingPage, ProjectPage
from mezzanine.pages.page_processors import processor_for

@processor_for(ProjectsLandingPage)
def pull_published_projects(request, page):
    published_projects = ProjectPage.objects.filter(status=2)

    return {'projects': published_projects}
     


