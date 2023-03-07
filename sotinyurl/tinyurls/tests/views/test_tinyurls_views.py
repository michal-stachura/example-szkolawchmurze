import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from sotinyurl.tinyurls.models import TinyUrl
from sotinyurl.tinyurls.tests.fixtures import tiny_url_fixture
from sotinyurl.tinyurls.tests.factories import TinyUrlFactory
from sotinyurl.tinyurls.serializers import TinyUrlSerializer, TinyUrlDetailSerializer
from sotinyurl.users.tests.fixtures import admin_fixture
from sotinyurl.users.models import User


test_tiny_url = tiny_url_fixture
admin_user = admin_fixture
pytestmark = pytest.mark.django_db

class TestTinyUrlViewSet:

    def setup_class(self):
        self.endpoint = reverse("tinyurls:tinyurl-list")
        self.api_client = APIClient()

    def test_list(self, admin_user: User) -> None:
        TinyUrlFactory.create_batch(10)

        response = self.api_client.get(self.endpoint)
        assert response.status_code == 403

        self.api_client.force_authenticate(
            user=admin_user
        )
        response = self.api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.data["results"]) == 10

    def test_create(self, admin_user: User) -> None:
        data = {
            "redirect_to": "https://not-existed-url.com"
        }

        self.api_client.force_authenticate(
            user=None
        )
        response = self.api_client.post(self.endpoint, data=data)
        assert response.status_code == 201

        self.api_client.force_authenticate(
            user=admin_user
        )
        response = self.api_client.post(self.endpoint, data=data)
        tiny_url = TinyUrl.objects.get(id=response.data["id"])
        serializer = TinyUrlDetailSerializer(tiny_url)

        assert response.status_code == 201
        assert response.data == serializer.data

    def test_retrieve(self, admin_user: User, test_tiny_url: TinyUrl) -> None:
        self.api_client.force_authenticate(
            user=None
        )
        url = f"{self.endpoint}{test_tiny_url.id}/"
        response = self.api_client.get(url)
        assert response.status_code == 403

        self.api_client.force_authenticate(
            user=admin_user
        )
        response = self.api_client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == str(test_tiny_url.id)
