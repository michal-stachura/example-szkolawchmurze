import pytest
from django.conf import settings
from django.urls import resolve, reverse

from sotinyurl.tinyurls.models import TinyUrl
from sotinyurl.tinyurls.tests.fixtures import tiny_url_fixture
from sotinyurl.tinyurls.views import TinyUrlViewSet

test_tiny_url = tiny_url_fixture
pytestmark = pytest.mark.django_db


class TestTinyUrlUrls:

    def test_list(list) -> None:
        """GET, POST"""
        assert (
            reverse("tinyurls:tinyurl-list")
            == f"/api/tinyurls/"
        )
        assert (
            resolve(f"/api/tinyurls/").view_name
            == "tinyurls:tinyurl-list"
        )
        assert (
            resolve(f"/api/tinyurls/").func.cls
            == TinyUrlViewSet
        )
    
    def test_detail(self, test_tiny_url: TinyUrl) -> None:
        """GET"""
        assert (
            reverse(
                "tinyurls:tinyurl-detail",
                kwargs={"id": str(test_tiny_url.id)}
            ) == f"/api/tinyurls/{str(test_tiny_url.id)}/"
        )
        assert (
            resolve(
                f"/api/tinyurls/{str(test_tiny_url.id)}/"
            ).view_name == "tinyurls:tinyurl-detail"
        )
        assert (
            resolve(
                f"/api/tinyurls/{str(test_tiny_url.id)}/"            
            ).func.cls == TinyUrlViewSet
        )
