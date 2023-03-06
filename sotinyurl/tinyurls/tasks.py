from config import celery_app
from sotinyurl.tinyurls.models import TinyUrl
from django.utils.timezone import now


@celery_app.task()
def delete_overdue_tiny_urls():
    """Remove all tiny urls which are overdue"""
    urls_to_delete = TinyUrl.objects.filter(
        valid_to__lt=now(),
        deleted_at__isnull=False
    )
    urls_to_delete.update(
        deleted_at=now(),
    )
