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
Issue - 3 commits with same changes. Commits ` c93ac1d`, `0a5d8ef` and `d5c30f7` are all the same commits. This is because I added creds.json to my gitignore file, but it still pushed to github. I then tried to reset my repo and IDE to before this using multiple commands in the terminal to no avail. To my knowledge there is no way to delete these commits. There is no sensitive information in this file which means it is not a critical error, but something I will have to be more careful with in the future. After fixing the filepath in gitignore, no difference has been made and the creds.json file still shows in the project repo. This is a mistake that I will learn from and ensure it does not happen in the future.

### Bug 05
Issue - Error when `python3 loaddata posts` command was run.
Cause - My `created_at` field was called `created_on`, causing an error as the fields didn't match.
Fix - Change field in creds.json file to `created_at` 