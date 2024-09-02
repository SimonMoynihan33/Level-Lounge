from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    """
    Represents a post in a forum thread.

    Each post is associated with a user and contains a title, content, 
    and timestamps for creation and updates. A slug field for
    creating user-friendly URLs. Code Institute Post model followed
    with some changes made.

    Attributes:
        title (CharField): The title of the post.
        slug (SlugField): A slugified version of the title for use in URLs.
        content (TextField): The main content of the post.
        created_at (DateTimeField): Timestamp when the post was created.
        updated_at (DateTimeField): Timestamp when the post was last updated.
        user (ForeignKey): Reference to the User who created the post.
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.IntegerField(choices=STATUS, default=0)