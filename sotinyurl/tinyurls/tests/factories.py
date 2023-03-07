import factory
from factory.django import DjangoModelFactory

from sotinyurl.tinyurls.models import TinyUrl

class TinyUrlFactory(DjangoModelFactory):
    
    class Meta:
        model = TinyUrl

    redirect_to = factory.Faker("url")
