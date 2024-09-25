## Bugs

### Bug 01
- Issue: `django.core.exceptions.ImproperlyConfigured: allauth.account.middleware.AccountMiddleware must be added to settings.MIDDLEWARE`.
- Cause: Django Allauth expected a specific middleware, `allauth.account.middleware.AccountMiddleware` to be added to 'MIDDLEWARE' settings.
- Fix: Add `'allauth.account.middleware.AccountMiddleware',`

### Bug 02
- Issue: When I try to add a comment through the Django admin site, I'm met with a Server Error (500). 
- Cause: When ```Debug=True``` was set, I was told my error was that the 'Comment' object has no attribute 'body'.
- Fix: Change attribute 'self.body' to 'self.content'.

### Bug 03
- Issue: When the comment was saved, an error that user was not defined showed.
- Cause: This was because I had defined 'author' in the model, but used 'user' in the template literal inside the dunder method of the Comment class.
- Fix: Define as user instead of author to keep consistency with other models.

### Bug 04 
- Issue: Three commits with same name and minute changes. Commits ` c93ac1d`, `0a5d8ef` and `d5c30f7` are all the same commits. This is because I added posts.json to my gitignore file, but it still pushed to github. All three of these commits were futile attempts at deleting the previous one, and updating it so that posts.json was no longer being pushed to Github. After realising this did not work and I could not delete these commits, I searched online for solutions. This was a lesson learned in that you cannot, to my knowledge, delete commits and not to try to re-do a previous commit logged.
- Cause: Wrong filepath for posts.json.
- Fix: After alot of searching online and speaking to some developers on stackoverflow, the solution I found was:
  1. Fix filepath in .gitignore
  2. Force Git to stop tracking the file with the command `git rm --cached level_lounge/fixtures/posts.json`
  3. Commit changes
  4. Verify file is gone by running `git status`

  I then had to remove the file from Git history and the main repo. To do this I:

  5. Had to run the filter ```git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch level_lounge/fixtures/posts.json" \
  --prune-empty --tag-name-filter cat -- --all```
  6. Clean the repo `git reflog expire --expire=now --all && git gc --prune=now --aggressive`
  7. Force push `git push --force`

This cleared the file from my repo and its history and stopped Git from tracking it in future commits.

### Bug 05
- Issue: Error when `python3 loaddata posts` command was run.
- Cause: My `created_at` field was called `created_on`, causing an error as the fields didn't match.
- Fix: Change field in creds.json file to `created_at`

### Bug 06
- Issue: Custom CSS file not applying to html page.
- Cause: MIME type error.
- Fix: To fix this I changed around the static path in settings.py to no avail, checked everything twice and all code was as it should be. I moved the static file into the my_project directory, and then moved it back into the top level of the directory which fixed the issue!.

### Bug 07 
- Issue: Comment form showing three times staxcked on top of eachother.
- Cause: 

### Bug 08
- Issue: Could not get comment content to show.
- Cause: Was referencing the content as 'body' when it is content in my model.
- Fix: Change 'body' tags to content throughout post_detail.html and py files.

### Bug 09 

A large bug I encountered was obtaining nested comments. The Code Institute walkthrough views and template did not support this feature, but I felt it was an essential aspect of a discussion based forum website. Most of the time, when I added a view or updated my post_detail template, I ecountered server errors or replies would not show at all.

### Bug 10
- Issue: `django.template.exceptions.TemplateDoesNotExist: comments.html` error shown when trying to run server when comments.html exists and has content.

### Bug 11
- Issue: `Not NULL` error when trying to comment for 'author'.

### Bug 12 
- Issue: `RecursionError` when attempting to comment.
- Cause: I created an infinite loop as I did not handle checks if there is no replies properly.
- Fix: Wrap the `{% include %}` tag in a conditional to check if there are replies.

### Bug 13
- Issue: `RecursionError` when attempting to reply to a comment.
- Cause: This was because I was not terminating the logic properly when displaying the replies, causing replies to display infinitely.
- Fix: Add for loop to comments.html to iterate through replies and end when there are no more replies, and call `exists()` method to make sure comment replies exist.

### Bug 14
- Issue: Too many replies can affect mobile view and does not look good. Applying hidden class using django templating language did seem to work in comments.html.
- Attempted fixes: My first attempt was to use django templating language to apply a css class to comments if there was more than three, but the syntax would not work due to the first `>` tag stopping the rest of the code from running in this example:
```
{% for reply in comment.replies.all %}
        <!-- Only show the first 3 replies initially, hide the rest -->
        <div class="reply {% if forloop.counter **>** 3 %}hidden-reply{% endif %}" id="reply-{{ reply.id }}">
            {% include 'level_lounge/comments.html' with comment=reply %}
        </div>
        {% endfor %}
```

I also tried running the loop outside of the div element to no avail. I also tried adding the `<style>` tag within the templating language but found the same issue as the first solution.

I changed my perspective and decided to try targetting with JavaScript which was fruitless.
- Cause: Drawbacks with templating language.
- Fix: After placing console.logs in my hideReplies function, I found that my `.reply` class was not being applied to each reply, therefore not being targetted by JavaScript or the CSS.

### Bug 15
- Issue: Committed changes and pushed them and the site was working, and when I open it again the next day thw fixed buttons are no longer working.
- Fix: Re-do all changes made previous day.

### Bug 16
- Issue: Cannot get edit post form to show when trying to change CI code from editting comments.

### Bug 17
- Issue: Cannot get Logout/Login list item to align centrally when the nav collapses on mobile devices. Only solutions I could think of with css aligned everything to the left, or would leave 'Home' and 'Profile' horizontal on one line, and 'Login' right aligned on the next line.
- Cause: Failure overriding Bootstrap styling successfully.
- Fix: The only fix I could think of was removing the `ms-auto` Bootstrap class depending on screen sizes. I achieved this through JavaScript.

### Bug 18
- Issue: Created UserProfile model and view after creating users.
- Cause: Implemented Profile feature last, after populating site for testing.
- Fix: Use python shell commands to loop through and create user profiles for each user without one.
----------------------- Image

### Bug 19
- Issue: Could not get default image to render on profile page.
- Cause: Media URL not working as intended.
- Fix: Add `'MEDIA_URL': settings.MEDIA_URL,` to profile_view directly.

### Bug 20
- Issue: Post count not updating on user profile.
- Cause: Post count feature and signals added after posts were created, therefore not counting posts already created.
- Fix: Run command in Django shell to iterate over posts and update the count.

### Bug 21
- Issue: Profile picture error when trying to access a post from a user created before default profile image was set.
- Cause: No Profile image for a user.
- Fix: Run django shell and input code: 

```
from level_lounge.models import UserProfile
default_image_path = 'profile_pics/default-avatar-icon.jpg'
# Query all profiles that don't have a profile picture set
profiles_without_images = UserProfile.objects.filter(profile_picture='')
# Update each profile to have the default image
for profile in profiles_without_images:
    profile.profile_picture = default_image_path
    profile.save()

print(f"Updated {profiles_without_images.count()} profiles with the default profile picture.")
```

Result: `Updated 4 profiles with the default profile picture.`

### Bug 22
- Issue: Profile images not rendering all of the time

