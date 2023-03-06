import random
import string
import datetime
from django.db import models
from django.conf import settings
from django.utils.timezone import now
from sotinyurl.utils.common_model import CommonModel
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

User = get_user_model()

class TinyUrl(CommonModel):

    tiny_url = models.URLField(
        max_length=50,
        editable=False,
        help_text=_("This is a Tiny URL")
    )
    redirect_to = models.URLField(
        max_length=200,
    )
    valid_to = models.DateTimeField(
        null=True,
        blank=True,
        default=(now() + datetime.timedelta(days=365))
    )
    owner = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ["created_at"]
        constraints = [
            models.UniqueConstraint(
                fields = ["tiny_url"],
                name = "%(app_label)s_%(class)s_unique_tiny_url",
                violation_error_message = _("Hey Bro this is not allowed. Tiny url must be unique!"),
            )
        ]

    def __str__(self) -> str:
        return f"{self.tiny_url} -> {self.redirect_to}"
    
    def __generate_random_tiny_url(length: int = settings.TINYURL_LENGTH) -> str:
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for i in range(settings.TINYURL_LENGTH))
        return f"{settings.DOMAIN_URL}/{random_string}"

    def __tiny_url_already_exists(self, url_to_check: str) -> bool:
        return TinyUrl.objects.filter(tiny_url=url_to_check).exists()

    def get_redirect_to(self, slug):
        tiny_url = f"{settings.DOMAIN_URL}/{slug}"
        redirect_to = None
        try:
            obj = TinyUrl.objects.get(
                tiny_url=tiny_url,
                valid_to__gte=now()
            )
            redirect_to = obj.redirect_to
        except TinyUrl.DoesNotExist:
            pass
        
        return redirect_to

    def save(self, *args, **kwargs) -> None:
        if self.is_being_created:
            random_url = self.__generate_random_tiny_url()
            while self.__tiny_url_already_exists(random_url):
                random_url = self.__generate_random_tiny_url()
            self.tiny_url = random_url
        super().save(*args, **kwargs)
