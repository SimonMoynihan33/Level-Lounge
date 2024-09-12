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