from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from sotinyurl.tinyurls.models import TinyUrl
from sotinyurl.tinyurls.serializers import TinyUrlSerializer, TinyUrlDetailSerializer


class TinyUrlViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    queryset = TinyUrl.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
            if self.action in ["retrieve", "create"]:
                return TinyUrlDetailSerializer
            return TinyUrlSerializer

def catch_tiny_url_view(request, slug):
    redirect_to = TinyUrl().get_redirect_to(slug)
    if redirect_to:
        return redirect(redirect_to)
    return HttpResponse(_(f"This tiny url does not exists or is overdue."))
    