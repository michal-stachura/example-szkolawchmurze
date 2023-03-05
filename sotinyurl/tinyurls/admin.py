from django.contrib import admin
from sotinyurl.tinyurls.models import TinyUrl


@admin.register(TinyUrl)
class TinyUrlAdmin(admin.ModelAdmin):
    list_display = ["__str__", "valid_to", "owner"]
    search_fields = ["id", "tiny_url", "redirect_to", "owner__username"]
    readonly_fields = ["tiny_url"]
