from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from cdhweb.projects.models import Project


class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        qs = Project.objects.published(for_user=self.request.user)
        return qs


class ProjectDetailView(DetailView):
    model = Project

    def get_queryset(self):
        return Project.objects.published(for_user=self.request.user)