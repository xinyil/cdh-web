from django.contrib import admin
from .models import StockLandingPage
from fileattach.models import FileAttachment
from mezzanine.generic.models import ThreadedComment
# Register your models here.

class FileAttachmentInline(admin.TabularInline):
    model = FileAttachment

@admin.register(StockLandingPage)
class StockLandingAdmin(admin.ModelAdmin):
    exclude = ('short_url', 'in_menus', 'login_required')    
    inlines = [
        FileAttachmentInline
    ]

admin.site.unregister(ThreadedComment)
