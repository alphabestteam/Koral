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
        create_new_basket(user)

def create_new_basket(user):
    # Create a new basket for the user after adding the current basket to shopping history
    new_basket = Basket.objects.create(user_id=user)
    new_basket.save()
    