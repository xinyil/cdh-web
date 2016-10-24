from django.contrib import admin

# Register your models here.
from .models import ProjectPage, Project, ProjectMember, ProjectsLandingPage, ProjectRole


admin.site.register(ProjectPage)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(ProjectsLandingPage)
admin.site.register(ProjectRole)
