from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a UserProfile automatically
    when a new User instance is created.
    """
    if created:
        # Default new users to the 'Member' role
        UserProfile.objects.create(user=instance, role='Member')