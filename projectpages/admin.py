from django.contrib import admin

# Register your models here.
from .models import ProjectPage, Project, ProjectMember, ProjectsLandingPage, ProjectRole


class ProjectPageInline(admin.StackedInline):
    model = ProjectPage
    max_num = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectPageInline,
    ]
    

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMember)
admin.site.register(ProjectRole)
admin.site.register(ProjectsLandingPage)
