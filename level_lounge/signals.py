from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CustomUserProfile  # Import your custom profile model

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal to automatically create or update the UserProfile whenever a User is created or updated.
    """
    if created:
        CustomUserProfile.objects.create(user=instance)  # Create a profile for the new user
    else:
        instance.profile.save()  # Save the profile when the user is updated