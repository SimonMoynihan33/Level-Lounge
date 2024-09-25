from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class UserProfile(models.Model):
    """
    Custom profile model that extends the User model with
    additional fields to meet custom criteria.

    Attributes:
        user (OneToOneField): Links to the Django User model.
        bio (TextField): Optional biography field for user descriptions.
        post_count (PositiveIntegerField): Tracks the number of posts
        created by the user.
        joined_on (DateTimeField): Records when the profile was created.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    profile_picture = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='https://res.cloudinary.com/dxckubce0/image/upload/v1/default-avatar-icon.webp'
        )
    post_count = models.PositiveIntegerField(
        default=0)  # Tracks user posts count
    # Timestamp of profile creation
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    """
    Represents a post in a forum thread.

    Each post is associated with a user and contains a title, content,
    and timestamps for creation and updates. A slug field for
    creating user-friendly URLs. Code Institute Post model followed
    with some changes made.

    Attributes:
        title (CharField): The title of the post.
        slug (SlugField): A slugified version of the title for use in
        URLs.
        content (TextField): The main content of the post.
        created_at (DateTimeField): Timestamp when the post was created.
        updated_at (DateTimeField): Timestamp when the post was last
        updated.
        user (ForeignKey): Reference to the User who created the post.
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically generate a slug
        from the post title if it doesn't already exist.

        The slug is generated using Django's slugify function, ensuring that
        it is URL-friendly and unique. After generating the slug, the original
        save method is called to save the post object to the database.
        """
        if not self.slug:  # Only set the slug if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the Post object, which is the
        post's title.

        This method is used to provide a human-readable representation of
        the object,
        making it easier to identify in the admin interface and during
        debugging.
        """
        return f"{self.title} | Written by {self.author}"


class Comment(models.Model):
    """
    Represents a comment on a post in the forum.

    Each comment is associated with a user and a post, and can optionally
    be a reply to another comment, supporting nested comment threads.

    Attributes:
        post (ForeignKey): The post that this comment is related to.
        user (ForeignKey): The user who created the comment.
        content (TextField): The main content of the comment.
        created_at (DateTimeField): The timestamp when the comment was
        created.
        parent (ForeignKey): A field for nesting comments as replies to
        other comments.
    """
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE,
        related_name='replies')

    def __str__(self):
        """
        Returns the string representation of the Comment object, which
        includes the username of the commenter
        and the title of the post the comment is associated with.
        This method provides a clear and concise representation of the
        comment, making it easier to identify
        in the Django admin interface and during debugging, especially
        when dealing with many comments.
        """
        return f'Comment "{self.content[:20]}..." by {self.user.username}\
        on {self.post.title}'

    class Meta:
        ordering = ['-created_at']
