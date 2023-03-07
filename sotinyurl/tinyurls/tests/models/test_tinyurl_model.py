import pytest
from sotinyurl.tinyurls.models import TinyUrl
from sotinyurl.tinyurls.tests.factories import TinyUrlFactory
from sotinyurl.tinyurls.tests.fixtures import tiny_url_fixture

pytestmark = pytest.mark.django_db
test_tiny_url = tiny_url_fixture

class TestTinyUrlModel:
    def test_tiny_url_add(self) -> None:
        tiny_url = TinyUrlFactory()
        assert tiny_url.id != ""

    def test_read_db(self, test_tiny_url: TinyUrl) -> None:
        obj = TinyUrl.objects.get(id=test_tiny_url.id)
        assert test_tiny_url == obj
    
    def test_soft_delete(self) -> None:
        TinyUrlFactory.create_batch(4)
        tiny_url_to_delete = TinyUrlFactory()

        assert TinyUrl.objects.all().count() == 5
        tiny_url_to_delete.delete()

        assert TinyUrl.objects.all().count() == 4
        assert TinyUrl.objects.with_deleted().count() == 5
        assert TinyUrl.objects.filter(id=str(tiny_url_to_delete.id)).count() == 0
        assert TinyUrl.objects.with_deleted().filter(id=str(tiny_url_to_delete.id)).count() == 1
    
    def test_hard_delete(self) -> None:
        TinyUrlFactory.create_batch(4)
        tiny_url_to_delete = TinyUrlFactory()
        
        assert TinyUrl.objects.all().count() == 5
        tiny_url_to_delete.delete_forever()

        assert TinyUrl.objects.all().count() == 4
        assert TinyUrl.objects.with_deleted().count() == 4

