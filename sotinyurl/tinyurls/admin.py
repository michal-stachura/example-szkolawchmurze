from django.contrib import admin
from sotinyurl.tinyurls.models import TinyUrl


@admin.register(TinyUrl)
class TinyUrlAdmin(admin.ModelAdmin):
    list_display = ["__str__", "valid_to", "owner", "deleted_at"]
    search_fields = ["id", "tiny_url", "redirect_to", "owner__username"]
    readonly_fields = ["tiny_url"]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return TinyUrl.objects.with_deleted()
        return super().get_queryset(request)
