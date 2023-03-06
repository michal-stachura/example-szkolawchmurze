import uuid
from faker import Faker
from django.conf import settings
from sotinyurl.tinyurls.models import TinyUrl
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()

tiny = TinyUrl()
fake = Faker()
env_name = settings.ENV_NAME or None

if env_name == "local" and not User.objects.filter(username="admin").exists():
    print ("Create local superuser")
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin"
    )

print ("Create Random Tiny Urls")
bulk_list = [
    TinyUrl(
        tiny_url=tiny._TinyUrl__generate_random_tiny_url(),
        redirect_to=fake.url(),
        created_at=now(),
        updated_at=now(),
        id=uuid.uuid4()
    )
    for x in range(10000)
]
TinyUrl.objects.bulk_create(bulk_list)
