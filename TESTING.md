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