from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Basket

@receiver(post_save, sender=Basket)
def update_shopping_history(sender, instance, created, **kwargs):
    if created:
        user = instance.user_id
        user.shopping_history.add(instance)
