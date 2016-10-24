from django.db import models
from mezzanine.core.fields import FileField

# Create your models here.

class FileAttachment(models.Model):
    attached_file  = FileField("Image, Document")
    display_name = models.CharField(max_length=255) 
    generic_template = models.ForeignKey("stocktemplate.StockLandingPage",
                                         on_delete=models.CASCADE,
                                         blank=True, null=True)
