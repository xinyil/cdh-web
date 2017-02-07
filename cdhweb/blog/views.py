from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import BlogPost


class BlogListView(ListView):

    # same list view can power complete list or filtered version
    # by year, month, whatever
    # - pass year/month/etc filters in context data for display
    #   in the template
    model = BlogPost

    def get_queryset(self):
        qs = BlogPost.objects.published(for_user=self.request.user)
        if self.kwargs.get('year', None):
            qs = qs.filter(publish_date__year=self.kwargs['year'])
        return qs


class BlogDetailView(DetailView):

    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.published(for_user=self.request.user)