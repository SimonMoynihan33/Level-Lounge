from django.db import models

# Create your models here.
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
        post_number(IntegerField): Show the amount of posts a user has created
        created_at (DateTimeField): The date and time when the user profile was created.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Returns the string representation of the UserProfile object, which is the associated user's username.
        
        This method provides a human-readable identifier for the UserProfile object, making it easier 
        to distinguish between different profiles in the Django admin interface and during debugging.
        """
        return self.user.username