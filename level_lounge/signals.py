from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Post  # Import your custom profile model

# Leveraged AI to create signals


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal to automatically create or update the UserProfile whenever a
    User is created or updated.
    """
    if created:
        # Create a profile for the new user
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()  # Save the profile when the user is updated


@receiver(post_save, sender=Post)
def update_post_count_on_create(sender, instance, created, **kwargs):
    """
    Updates user's post count when a new post is created.
    """
    if created:
        user_profile = UserProfile.objects.get(user=instance.author)
        user_profile.post_count = Post.objects.filter(
            author=instance.author).count()
        user_profile.save()


@receiver(post_delete, sender=Post)
def update_post_count_on_delete(sender, instance, **kwargs):
    """
    Updates user's post count when a post is deleted.
    """
    user_profile = UserProfile.objects.get(user=instance.author)
    user_profile.post_count = Post.objects.filter(
        author=instance.author).count()
    user_profile.save()
