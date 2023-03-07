import pytest

from sotinyurl.tinyurls.models import TinyUrl
from sotinyurl.tinyurls.tests.factories import TinyUrlFactory

@pytest.fixture
def tiny_url_fixture(db) -> TinyUrl:
    return TinyUrlFactory()