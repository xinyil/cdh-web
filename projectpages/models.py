from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.core.models import Displayable

class Project(models.Model):   
    project_title = models.CharField(max_length=255)
    project_subtitle = models.CharField(max_length=80, blank=True, null=True)
    project_summary = models.CharField(max_length=255)
    project_description = RichTextField()
    project_create_update = models.DateField()
    

    def __str__(self):
        return self.project_title

    class Meta:
        ordering = ('-project_create_update',)

class ProjectRole(models.Model):
    title = models.CharField(max_length=255)
    rank = models.IntegerField()

    def __str__(self):
        return self.title + ": " + str(self.rank) 
    
    class Meta:
        verbose_name = 'Project Role'

class ProjectMember(models.Model):
    name = models.CharField(max_length=255)
    project = models.ManyToManyField(Project)
    project_role = models.ForeignKey(ProjectRole)

    def __str__(self):
        return self.project_role.title+': '+self.name
    
    class Meta:
        ordering = ('-project_role__rank',)
        verbose_name = 'Project Member'

class ProjectPage(Displayable):
    project_data = models.ForeignKey(Project)
    project_content = RichTextField()
    project_image = FileField(format="Image")
    override_image = FileField(format="Image", blank=True, null=True)
    title = models.CharField(max_length=500, default='CDH @ Princeton Projects')
    def get_absolute_url(self):
        name = '/projects/' + self.project_data.project_title.replace(' ', '').lower()
        return name

    class Meta:
        ordering = ('-project_data__project_create_update',)

class ProjectsLandingPage(Page):
    class Meta:
        verbose_name = 'Project List'
