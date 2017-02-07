from django.contrib import admin
from .models import StaffLandingPage, Staffer, StafferPage


class StafferPageInline(admin.StackedInline):
    model = StafferPage
    max_num = 1
    fields = ('title', 'status', 'publish_date', 'expiry_date', 'extra_content')

class StafferAdmin(admin.ModelAdmin):
    inlines = [
        StafferPageInline,
    ]


# Register your models here.
admin.site.register(StaffLandingPage)
admin.site.register(Staffer, StafferAdmin)
