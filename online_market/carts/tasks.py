from celery import shared_task
from django.utils.timezone import now
from datetime import timedelta
from carts.models import Cart

@shared_task
def clean_inactive_carts():
    threshold_date = now() - timedelta(days=30)
    inactive_carts = Cart.objects.filter(updated_at__lt=threshold_date, status='active')
    deleted_count = inactive_carts.delete()[0]
    return f'{deleted_count} inactive carts deleted.'
