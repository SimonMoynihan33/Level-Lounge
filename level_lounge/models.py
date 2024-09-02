from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    """
    Extends the built-in Django User model to include additional fields for the user profile.
    
    This model is linked to the Django User model via a OneToOne relationship and includes fields
    for storing additional user information, such as a bio and a profile picture. The `created_at`
    field automatically stores the timestamp when the profile was created.
    
    Attributes:
        user (OneToOneField): Links to the Django User model. Used from Django documentation.
        bio (TextField): A short biography or description provided by the user. Optional.
        profile_picture (ImageField): An image file for the user's profile picture. Optional.
        created_at (DateTimeField): The date and time when the user profile was created.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username