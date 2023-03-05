import random
import string
import uuid

from django_seed import Seed
from sotinyurl.tinyurls.models import TinyUrl
from django.conf import settings
from django.utils.timezone import now

seeder = Seed.seeder()
tiny = TinyUrl()

bulk_list = [
    TinyUrl(
        tiny_url=tiny._TinyUrl__generate_random_tiny_url(),
        redirect_to=seeder.faker.url(),
        created_at=now(),
        updated_at=now(),
        id=uuid.uuid4()
    )
    for x in range(10000)
]
TinyUrl.objects.bulk_create(bulk_list)
