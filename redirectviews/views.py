from django.shortcuts import render, get_object_or_404
from django.views.generic.base import RedirectView
from mezzanine.blog.models import BlogPost

# Create your views here
class BlogSlugRedirectView(RedirectView):
    permanent = True
    pattern_name = 'blogslug-redirect'
    def get_redirect_url(self, *args, **kwargs):
        blog_post = get_object_or_404(BlogPost, status=2, slug=kwargs['slug'])
        print(blog_post)
        self.url = blog_post.get_absolute_url()
        print(self.url)
        return super(BlogSlugRedirectView, self).get_redirect_url(*args, **kwargs)

