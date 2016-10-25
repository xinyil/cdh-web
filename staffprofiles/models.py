from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import Displayable
from mezzanine.core.fields import RichTextField, FileField
# Create your models here.


# Core functionality for staff members
class Staffer(models.Model):
    name = models.CharField(max_length=255)
    photo = FileField(format="Image")
    profile_photo = FileField(format="Image", blank=True, null=True)
    title = models.CharField(max_length=255)
    full_title = models.CharField(max_length=255,  blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    education = models.CharField(max_length=500, blank=True, null=True)
    sortorder = models.IntegerField()

    def __str__(self):
        return self.title + ': ' + self.name


# List of specialties, many to many on Staffer
class Specialty(models.Model):
    technology = models.CharField(max_length=500)
    staff_member = models.ManyToManyField(Staffer)


# Create a page to 'publish' the staff member
class StafferPage(Displayable):
    staffer_data = models.ForeignKey(Staffer)
    extra_content = RichTextField()

    def get_absolute_url(self):
        return '/about/staff/' + self.staffer_data.name.lower().replace(' ', '-')

    class Meta:
        ordering = ['-staffer_data__sortorder']


class StaffLandingPage(Page):
    pass
