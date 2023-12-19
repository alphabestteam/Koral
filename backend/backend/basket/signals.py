from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Basket

User = get_user_model()

@receiver(post_save, sender=Basket)
def update_shopping_history(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(pk=instance.user_id)
        user.shopping_history.add(instance)
