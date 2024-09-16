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
    # search_tag = models.TextField (for later addition)
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
        
        The slug is generated using Django's slugify function, ensuring that it is 
        URL-friendly and unique. After generating the slug, the original save method 
        is called to save the post object to the database.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the Post object, which is the post's title.
        
        This method is used to provide a human-readable representation of the object,
        making it easier to identify in the admin interface and during debugging.
        """
        return f"{self.title} | Written by {self.author}"


class Comment(models.Model):
    """
    Represents a comment on a post in the forum.

    Each comment is associated with a user and a post, and can optionally be
    a reply to another comment, supporting nested comment threads.

    Attributes:
        post (ForeignKey): The post that this comment is related to.
        user (ForeignKey): The user who created the comment.
        content (TextField): The main content of the comment.
        created_at (DateTimeField): The timestamp when the comment was created.
        parent (ForeignKey): A field for nesting comments as replies to other comments.
    """
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        """
        Returns the string representation of the Comment object, which includes the username of the commenter 
        and the title of the post the comment is associated with.

        This method provides a clear and concise representation of the comment, making it easier to identify 
        in the Django admin interface and during debugging, especially when dealing with many comments.
        """
        return f'Comment "{self.content[:20]}..." by {self.user.username} on {self.post.title}'

    class Meta:
        """
        Defines the default ordering for Comment objects, arranging them by their creation time in ascending order.
        This ensures that comments are displayed in chronological order, with the oldest comments appearing first.
        """
        ordering = ['-created_at']