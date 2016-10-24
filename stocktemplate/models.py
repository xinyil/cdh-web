from django.db import models
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.pages.models import Page

# Create your models here.

class StockLandingPage(Page):
    image  = FileField("Image", format="Image", blank=True, null=True)
    content = RichTextField()

    class Meta:
        verbose_name = 'Generic Page'
        verbose_name_plural = 'Generic Pages'
        
