from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)

from sotinyurl.tinyurls.models import TinyUrl
from sotinyurl.tinyurls.serializers import TinyUrlSerializer


class TinyUrlViewSet(
    GenericViewSet,
    ListModelMixin
):
    queryset = TinyUrl.objects.all()
    serializer_class = TinyUrlSerializer

