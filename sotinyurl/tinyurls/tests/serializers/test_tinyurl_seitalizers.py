import factory
import pytest

from sotinyurl.tinyurls.models import TinyUrl
from sotinyurl.tinyurls.serializers import TinyUrlSerializer, TinyUrlDetailSerializer
from sotinyurl.tinyurls.tests.factories import TinyUrlFactory
from sotinyurl.tinyurls.tests.fixtures import tiny_url_fixture

pytestmark = pytest.mark.django_db
test_tiny_url = tiny_url_fixture

class TestTinyUrlSerializer:

    def test_serialize_model(self) -> None:
        test_tiny_url = TinyUrlFactory()
        serializer = TinyUrlSerializer(test_tiny_url)

        assert serializer.data
        assert set(serializer.data.keys()) == set(
            ["id", "tiny_url", "redirect_to"]
        )

    def test_serialize_data(self) -> None:

        valid_seialized_data = factory.build(dict, FACTORY_CLASS=TinyUrlFactory)
        
        serializer = TinyUrlSerializer(data=valid_seialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}


class TestTinyUrlDetailSerializer:

    def test_serialize_model(self) -> None:
        test_tiny_url = TinyUrlFactory()
        serializer = TinyUrlDetailSerializer(test_tiny_url)

        assert serializer.data
        assert set(serializer.data.keys()) == set(
            ["id", "tiny_url", "redirect_to","valid_to", "owner", "created_at", "updated_at"]
        )

    def test_serialize_data(self) -> None:

        valid_seialized_data = factory.build(dict, FACTORY_CLASS=TinyUrlFactory)
        
        serializer = TinyUrlDetailSerializer(data=valid_seialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}
