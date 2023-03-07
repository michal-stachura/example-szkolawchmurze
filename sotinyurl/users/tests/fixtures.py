import pytest

from sotinyurl.users.models import User
from sotinyurl.users.tests.factories import UserFactory

@pytest.fixture
def admin_fixture(db) -> User:
    return UserFactory(
        username="admin",
        is_superuser=True,
        is_active=True,
        is_staff=True,
        email="admin@example.com"
    )
