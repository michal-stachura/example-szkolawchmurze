from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sotinyurl.tinyurls.views import TinyUrlViewSet

app_name = "tinyurls"
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("", TinyUrlViewSet)

urlpatterns = router.urls
